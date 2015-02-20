Title: CUDA 6.5 starter example with timing and Unified Memory access.
Date: 2015-02-20 23:00
Category: Programming
Tags: CUDA
Author: Jianming

Now, I'm on the Chinese New Year holiday, got some time to learn CUDA which I left it behind for long time.

I found the [CUDA Programing Doc](docs.nvidia.com/cuda/cuda-c-programming-guide/index.html) doesn't present a complete unified memory code.

Here is the a [blog article](http://devblogs.nvidia.com/parallelforall/unified-memory-in-cuda-6/) about the unified memory in the CUDA 6+, so what I did here is just implementing this developer friendly feature merging with the working method of timing both GPU kernal run time and the same function on CPU's run time. 

So we implement a 1000k array addition operator here.


Firstly, the data format is like this,
    :::c++
    const int arraySize = 1000000;
    struct LargeData
    {
	    int hugevalue[arraySize] ;
    };

Then the memory allocation for Unified Memory Access is simply,

    :::c++
    LargeData *a;
    cudaMallocManaged((void**)&a, sizeof(LargeData));

see, no more code for explicitly copying around :). And after this, we can modify the data on the host memory, it will be automatically delivered to the GPU.

    :::c++
    __global__
    void addall(LargeData * a, LargeData * b, LargeData * c)
    {
	    int i = threadIdx.x;
	    int j = blockIdx.x ;
        //the index is calculated from consiering the block position and thread index
	    c->hugevalue[j * blockDim.x + i] = a->hugevalue[j * blockDim.x + i] + b->hugevalue[j * blockDim.x + i];
    }

    void launchAdd(LargeData * a, LargeData * b, LargeData * c)
    {
	
	    dim3 threadsPerBlock(256, 1);
	    dim3 numBlocks(arraySize / threadsPerBlock.x + 1, 1);

	    addall << <numBlocks, threadsPerBlock >> >(a, b, c);
	    cudaDeviceSynchronize();
    }
    int main()
    {
        LargeData *a;
	    LargeData *b;
	    LargeData *c;

	    cudaMallocManaged((void**)&a, sizeof(LargeData));
	    cudaMallocManaged((void**)&b, sizeof(LargeData));
	    cudaMallocManaged((void**)&c, sizeof(LargeData));

	    for (size_t i = 0; i < arraySize; ++i)
	    {
		    a->hugevalue[i] = i;
		    b->hugevalue[i] = i+1;
		    c->hugevalue[i] = 0;
	    }
	
	    launchAdd(a, b, c);

	    cudaFree(a);
	    cudaFree(b);
	    cudaFree(c);

	    cudaDeviceReset();

	    return 0;
    }


And to time the execution time, we use the code from [timing CUDA event](http://stackoverflow.com/a/7881320/921082) and [timing CPU](http://stackoverflow.com/a/17440673/921082) .

    :::c++
    //  Windows
    #ifdef _WIN32
    #include <Windows.h>
    double get_wall_time(){
	    LARGE_INTEGER time, freq;
	    if (!QueryPerformanceFrequency(&freq)){
		    //  Handle error
		    return 0;
	    }
	    if (!QueryPerformanceCounter(&time)){
		    //  Handle error
		    return 0;
	    }
	    return (double)time.QuadPart / freq.QuadPart;
    }
    double get_cpu_time(){
	    FILETIME a, b, c, d;
	    if (GetProcessTimes(GetCurrentProcess(), &a, &b, &c, &d) != 0){
		    //  Returns total user time.
		    //  Can be tweaked to include kernel times as well.
		    return
			    (double)(d.dwLowDateTime |
			    ((unsigned long long)d.dwHighDateTime << 32)) * 0.0000001;
	    }
	    else{
		    //  Handle error
		    return 0;
	    }
    }

    //  Posix/Linux
    #else
    #include <sys/time.h>
    double get_wall_time(){
	    struct timeval time;
	    if (gettimeofday(&time, NULL)){
		    //  Handle error
		    return 0;
	    }
	    return (double)time.tv_sec + (double)time.tv_usec * .000001;
    }
    double get_cpu_time(){
	    return (double)clock() / CLOCKS_PER_SEC;
    }
    #endif

    void cpuAdd()
    {
	    //start cpu computation
	    printf("Start CPU \n");

	    for (size_t i = 0; i < arraySize; ++i)
	    {
		    aa[i] = i;
		    bb[i] = i + 1;
	    }

	    double wall_time0, wall_time1;
	    double cpu_time0, cpu_time1;

	    wall_time0 = get_wall_time();
	    cpu_time0 = get_cpu_time();

	    for (size_t i = 0; i < arraySize; ++i)
		    cc[i] = aa[i] + bb[i];

	    wall_time1 = get_wall_time();
	    cpu_time1 = get_cpu_time();

	    printf("=== CPU ===\n");
	    printf("CPU -- Wall time: %3.10f ms \n", (wall_time1 - wall_time0) * 1000);
	    printf("CPU -- Cpu time: %3.10f ms \n", (cpu_time1 - cpu_time0) * 1000);
    }


    void launchAdd(LargeData * a, LargeData * b, LargeData * c)
    {
	    float time;
	    double wall_time0, wall_time1;
	    double cpu_time0, cpu_time1;
	    cudaEvent_t start, stop;

	    dim3 threadsPerBlock(256, 1);
	    dim3 numBlocks(arraySize / threadsPerBlock.x + 1, 1);

	    wall_time0 = get_wall_time();
	    cpu_time0 = get_cpu_time();

	    HANDLE_ERROR(cudaEventCreate(&start));
	    HANDLE_ERROR(cudaEventCreate(&stop));
	    HANDLE_ERROR(cudaEventRecord(start, 0));

	    addall << <numBlocks, threadsPerBlock >> >(a, b, c);
	    cudaDeviceSynchronize();

	    HANDLE_ERROR(cudaEventRecord(stop, 0));
	    HANDLE_ERROR(cudaEventSynchronize(stop));
	    HANDLE_ERROR(cudaEventElapsedTime(&time, start, stop));

	    wall_time1 = get_wall_time();
	    cpu_time1 = get_cpu_time();

	    printf("=== CUDA Execution Time: ===\n");
	    printf("Cuda event time to generate:  %3.10f ms \n", time);
	    printf("Wall time: %3.10f ms \n", (wall_time1 - wall_time0) * 1000);
	    printf("Cpu time: %3.10f ms \n", (cpu_time1 - cpu_time0) * 1000);
    }

At last, you can find the complete source code from [github](https://github.com/tomriddle1234/cuda_examples/blob/master/arrayAdd_UnifiedMemory.cu).

The resul I got is for 1000k array,

```
Start CPU
=== CPU ===
CPU -- Wall time: 5.6946210389 ms
CPU -- Cpu time: 0.0000000000 ms
=== CUDA Execution Time: ===
Cuda event time to generate:  0.5817599893 ms
Wall time: 8.6047964578 ms
Cpu time: 0.0000000000 ms
```




	
