; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i1
  store i1 0, i1* %".2"
  br i1 1, label %"main.if", label %"main.endif"
main.if:
  %".5" = alloca i32
  store i32 3, i32* %".5"
  br label %"main.endif"
main.endif:
  %".8" = load i1, i1* %".2"
  br i1 %".8", label %"main.endif.if", label %"main.endif.endif"
main.endif.if:
  %".10" = alloca i32
  store i32 5, i32* %".10"
  br label %"main.endif.endif"
main.endif.endif:
  ret i32 0
}
