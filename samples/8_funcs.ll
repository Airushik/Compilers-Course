; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  call void (i32, i32, ...) @"foo"(i32 7, i32 3)
  ret i32 0
}

declare i32 @"printf"(...)

define void @"foo"(i32 %".1", i32 %".2", ...)
{
main.foo:
  %".4" = alloca i32
  store i32 %".1", i32* %".4"
  %".6" = alloca i32
  store i32 %".2", i32* %".6"
  %".8" = load i32, i32* %".4"
  %".9" = load i32, i32* %".6"
  %".10" = add i32 %".8", %".9"
  %".11" = alloca [3 x i8]
  store [3 x i8] c"%i\00", [3 x i8]* %".11"
  %".13" = getelementptr [3 x i8], [3 x i8]* %".11", i32 0, i32 0
  %".14" = call i32 (...) @"printf"(i8* %".13", i32 %".10")
  ret void
}
