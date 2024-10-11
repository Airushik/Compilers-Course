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
  br i1 %".8", label %"main.loop_end", label %"main.loop_body"
main.loop_body:
  %".10" = load i32, i32* %".4"
  store i32 %".10", i32* %".2"
  %".12" = load i32, i32* %".2"
  %".13" = icmp eq i32 %".12", 3
  br i1 %".13", label %"main.loop_body.if", label %"main.loop_body.endif"
main.loop_end:
  %".20" = load i32, i32* %".2"
  %".21" = alloca [3 x i8]
  store [3 x i8] c"%i\00", [3 x i8]* %".21"
  %".23" = getelementptr [3 x i8], [3 x i8]* %".21", i32 0, i32 0
  %".24" = call i32 (...) @"printf"(i8* %".23", i32 %".20")
  ret i32 0
main.loop_update:
  %".17" = add i32 %".7", 1
  store i32 %".17", i32* %".4"
  br label %"main.loop_cond"
main.loop_body.if:
  br label %"main.loop_end"
main.loop_body.endif:
  br label %"main.loop_update"
}

declare i32 @"printf"(...)
