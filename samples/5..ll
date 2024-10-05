; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 2, i32* %".2"
  %".4" = alloca i32
  store i32 1, i32* %".4"
  %".6" = load i32, i32* %".2"
  %".7" = load i32, i32* %".4"
  %".8" = icmp sgt i32 %".6", %".7"
  br i1 %".8", label %"main.if", label %"main.endif"
main.if:
  %".10" = sitofp i32 2 to double
  %".11" = fcmp ogt double 0x3ff3333333333333, %".10"
  %".12" = alloca i1
  store i1 %".11", i1* %".12"
  br label %"main.endif"
main.endif:
  ret i32 0
}
