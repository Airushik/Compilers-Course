; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  br i1 1, label %"main.if", label %"main.endif"
main.if:
  %".3" = alloca [8 x i8]
  store [8 x i8] c"Always \00", [8 x i8]* %".3"
  %".5" = getelementptr [8 x i8], [8 x i8]* %".3", i32 0, i32 0
  %".6" = call i32 (...) @"printf"(i8* %".5")
  br label %"main.endif"
main.endif:
  %".8" = alloca i1
  store i1 0, i1* %".8"
  %".10" = load i1, i1* %".8"
  br i1 1, label %"main.endif.if", label %"main.endif.endif"
main.endif.if:
  %".12" = alloca [8 x i8]
  store [8 x i8] c"Always \00", [8 x i8]* %".12"
  %".14" = getelementptr [8 x i8], [8 x i8]* %".12", i32 0, i32 0
  %".15" = call i32 (...) @"printf"(i8* %".14")
  br label %"main.endif.endif"
main.endif.endif:
  store i1 1, i1* %".8"
  %".18" = load i1, i1* %".8"
  br i1 1, label %"main.endif.endif.if", label %"main.endif.endif.endif"
main.endif.endif.if:
  %".20" = alloca [8 x i8]
  store [8 x i8] c"Always \00", [8 x i8]* %".20"
  %".22" = getelementptr [8 x i8], [8 x i8]* %".20", i32 0, i32 0
  %".23" = call i32 (...) @"printf"(i8* %".22")
  br label %"main.endif.endif.endif"
main.endif.endif.endif:
  ret i32 0
}

declare i32 @"printf"(...)
