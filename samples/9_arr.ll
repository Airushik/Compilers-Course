; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca [3 x i32]
  store [3 x i32] [i32 10, i32 12, i32 13], [3 x i32]* %".2"
  %".4" = sub i32 3, 1
  %".5" = getelementptr [3 x i32], [3 x i32]* %".2", i32 0, i32 %".4"
  %".6" = load i32, i32* %".5"
  %".7" = alloca i32
  store i32 %".6", i32* %".7"
  %".9" = load i32, i32* %".7"
  %".10" = alloca [3 x i8]
  store [3 x i8] c"%i\00", [3 x i8]* %".10"
  %".12" = getelementptr [3 x i8], [3 x i8]* %".10", i32 0, i32 0
  %".13" = call i32 (...) @"printf"(i8* %".12", i32 %".9")
  ret i32 0
}

declare i32 @"printf"(...)
