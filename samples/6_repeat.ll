; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 1, i32* %".2"
  br label %"main.loop_body"
main.loop_cond:
  %".9" = load i32, i32* %".2"
  %".10" = icmp slt i32 %".9", 0
  br i1 %".10", label %"main.loop_body", label %"main.loop_end"
main.loop_body:
  %".5" = load i32, i32* %".2"
  %".6" = add i32 %".5", 1
  store i32 %".6", i32* %".2"
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
