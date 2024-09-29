; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 2, i32* %".2"
  %".4" = load i32, i32* %".2"
  %".5" = fptosi double 0x400a666666666666 to i32
  store i32 %".5", i32* %".2"
  %".7" = load i32, i32* %".2"
  store i32 4, i32* %".2"
  ret i32 0
}
