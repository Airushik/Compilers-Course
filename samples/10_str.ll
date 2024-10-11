; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca [5 x i8]
  store [5 x i8] c"Mya!\00", [5 x i8]* %".2"
  %".4" = load [5 x i8], [5 x i8]* %".2"
  %".5" = alloca [5 x i8]
  store [5 x i8] %".4", [5 x i8]* %".5"
  %".7" = getelementptr [5 x i8], [5 x i8]* %".5", i32 0, i32 0
  %".8" = call i32 (...) @"printf"(i8* %".7")
  ret i32 0
}

declare i32 @"printf"(...)
