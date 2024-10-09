; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 1, i32* %".2"
  br label %"main.loop_cond"
main.loop_cond:
  %".5" = load i32, i32* %".2"
  %".6" = icmp slt i32 %".5", 5
  br i1 %".6", label %"main.loop_body", label %"main.loop_end"
main.loop_body:
  %".8" = load i32, i32* %".2"
  %".9" = load i32, i32* %".2"
  %".10" = add i32 %".9", 1
  store i32 %".10", i32* %".2"
  br label %"main.loop_cond"
main.loop_end:
  ret i32 0
}
