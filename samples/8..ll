; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 1, i32* %".2"
  %".4" = alloca i32
  store i32 1, i32* %".4"
  br label %"main.loop_cond"
main.loop_cond:
  %".7" = load i32, i32* %".4"
  %".8" = icmp sgt i32 %".7", 5
  br i1 %".8", label %"main.loop_body", label %"main.loop_end"
main.loop_body:
  %".10" = load i32, i32* %".2"
  %".11" = load i32, i32* %".2"
  %".12" = load i32, i32* %".4"
  %".13" = add i32 %".11", %".12"
  store i32 %".13", i32* %".2"
  br label %"main.loop_update"
main.loop_end:
  ret i32 0
main.loop_update:
  %".16" = add i32 %".7", 1
  store i32 %".16", i32* %".4"
  br label %"main.loop_cond"
}
