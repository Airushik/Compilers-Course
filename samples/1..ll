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
  ret i32 0
}
