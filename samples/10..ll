; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 4, i32* %".2"
  %".4" = load i32, i32* %".2"
  store i32 5, i32* %".2"
  ret i32 0
}

define void @"foo"()
{
main.foo:
  %".2" = load i32, i32* %".2"
  store i32 3, i32* %".2"
  ret void
}
