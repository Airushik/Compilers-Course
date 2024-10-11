; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca double
  store double 0x3fc999999999999a, double* %".2"
  %".4" = alloca double
  store double 0x3fc999999999999a, double* %".4"
  %".6" = alloca i32
  store i32 4, i32* %".6"
  %".8" = alloca i1
  store i1 1, i1* %".8"
  %".10" = alloca i1
  store i1 0, i1* %".10"
  %".12" = alloca [5 x i8]
  store [5 x i8] c"Myau\00", [5 x i8]* %".12"
  %".14" = alloca i32
  store i32 4, i32* %".14"
  %".16" = load i32, i32* %".14"
  %".17" = alloca [3 x i8]
  store [3 x i8] c"%i\00", [3 x i8]* %".17"
  %".19" = getelementptr [3 x i8], [3 x i8]* %".17", i32 0, i32 0
  %".20" = call i32 (...) @"printf"(i8* %".19", i32 %".16")
  ret i32 0
}

declare i32 @"printf"(...)
