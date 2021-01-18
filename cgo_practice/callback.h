#include<stdio.h>
#include <unistd.h>

typedef void (*callback)(void*);

static void call_pmdb_read(callback cb, void* data) {
  cb(data);
}

static void call_pmdb_exec(callback cb, void* data, char *str1, char *str2) {
  cb(data);
}
