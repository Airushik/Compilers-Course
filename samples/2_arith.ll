; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = sub i32 0, 1
  %".3" = alloca i32
  store i32 %".2", i32* %".3"
  %".5" = sub i32 2, 1
  %".6" = add i32 3, %".5"
  store i32 %".6", i32* %".3"
  %".8" = load i32, i32* %".3"
  %".9" = sdiv i32 7, 2
  %".10" = mul i32 %".8", %".9"
  %".11" = alloca i32
  store i32 %".10", i32* %".11"
  %".13" = load i32, i32* %".11"
  %".14" = alloca [4 x i8]
  store [4 x i8] c"%i \00", [4 x i8]* %".14"
  %".16" = getelementptr [4 x i8], [4 x i8]* %".14", i32 0, i32 0
  %".17" = call i32 (...) @"printf"(i8* %".16", i32 %".13")
  %".18" = load i32, i32* %".11"
  %".19" = srem i32 %".18", 3
  %".20" = alloca [3 x i8]
  store [3 x i8] c"%i\00", [3 x i8]* %".20"
  %".22" = getelementptr [3 x i8], [3 x i8]* %".20", i32 0, i32 0
  %".23" = call i32 (...) @"printf"(i8* %".22", i32 %".19")
  ret i32 0
}

declare i32 @"printf"(...)
