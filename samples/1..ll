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
  %".12" = load double, double* %".2"
  %".13" = alloca i32
  store i32 3, i32* %".13"
  %".15" = load i32, i32* %".13"
  store i32 4, i32* %".13"
  ret i32 0
}
