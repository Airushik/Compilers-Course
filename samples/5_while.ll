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
  %".9" = add i32 %".8", 1
  store i32 %".9", i32* %".2"
  br label %"main.loop_cond"
main.loop_end:
  %".12" = load i32, i32* %".2"
  %".13" = alloca [3 x i8]
  store [3 x i8] c"%i\00", [3 x i8]* %".13"
  %".15" = getelementptr [3 x i8], [3 x i8]* %".13", i32 0, i32 0
  %".16" = call i32 (...) @"printf"(i8* %".15", i32 %".12")
  ret i32 0
}

declare i32 @"printf"(...)
