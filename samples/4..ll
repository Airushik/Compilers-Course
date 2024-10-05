; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = sub i32 0, 4
  %".3" = alloca i32
  store i32 %".2", i32* %".3"
  %".5" = load i32, i32* %".3"
  %".6" = fadd i32 %".5", 1
  %".7" = add i32 2, %".6"
  %".8" = alloca i32
  store i32 %".7", i32* %".8"
  ret i32 0
}
