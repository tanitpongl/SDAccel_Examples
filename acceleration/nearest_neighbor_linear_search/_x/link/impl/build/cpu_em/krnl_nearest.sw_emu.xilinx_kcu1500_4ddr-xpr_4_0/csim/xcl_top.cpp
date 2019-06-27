#include "libspir_types.h"
#define EXPORT_PIPE_SYMBOLS 1
#include "cpu_pipes.h"
#undef EXPORT_PIPE_SYMBOLS
#include "xcl_half.h"
#include <cstddef>
#include <vector>
#include <pthread.h>

extern "C" {

void krnl_linear_search(size_t targets, size_t queries, size_t indices);

static pthread_mutex_t __xlnx_cl_krnl_linear_search_mutex = PTHREAD_MUTEX_INITIALIZER;
void __stub____xlnx_cl_krnl_linear_search(char **argv) {
  void **args = (void **)argv;
  size_t targets = *((size_t*)args[0+1]);
  size_t queries = *((size_t*)args[1+1]);
  size_t indices = *((size_t*)args[2+1]);
  pthread_mutex_lock(&__xlnx_cl_krnl_linear_search_mutex);
  krnl_linear_search(targets, queries, indices);
  pthread_mutex_unlock(&__xlnx_cl_krnl_linear_search_mutex);
}
}
