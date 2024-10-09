; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 5, i32* %".2"
  %".4" = alloca i32
  store i32 1, i32* %".4"
  %".6" = alloca i32
  store i32 1, i32* %".6"
  %".8" = alloca i32
  store i32 1, i32* %".8"
  %".10" = load i32, i32* %".2"
  br label %"main.loop_cond"
main.loop_cond:
  %".12" = load i32, i32* %".8"
  %".13" = icmp sgt i32 %".12", %".10"
  br i1 %".13", label %"main.loop_body", label %"main.loop_end"
main.loop_body:
  %".15" = load i32, i32* %".4"
  %".16" = load i32, i32* %".6"
  %".17" = add i32 %".15", %".16"
  %".18" = alloca i32
  store i32 %".17", i32* %".18"
  %".20" = load i32, i32* %".6"
  %".21" = load i32, i32* %".4"
  store i32 %".21", i32* %".6"
  %".23" = load i32, i32* %".4"
  %".24" = load i32, i32* %".18"
  store i32 %".24", i32* %".4"
  br label %"main.loop_update"
main.loop_end:
  ret i32 0
main.loop_update:
  %".27" = add i32 %".12", 1
  store i32 %".27", i32* %".8"
  br label %"main.loop_cond"
}
