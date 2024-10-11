; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca i32
  store i32 3, i32* %".2"
  %".4" = alloca i32
  store i32 4, i32* %".4"
  %".6" = alloca i32
  store i32 5, i32* %".6"
  %".8" = alloca i32
  store i32 5, i32* %".8"
  %".10" = load i32, i32* %".2"
  %".11" = load i32, i32* %".4"
  %".12" = load i32, i32* %".6"
  %".13" = load i32, i32* %".8"
  %".14" = icmp sle i32 %".12", %".13"
  %".15" = sext i1 %".14" to i32
  %".16" = mul i32 %".11", %".15"
  %".17" = icmp sge i32 %".10", %".16"
  br i1 %".17", label %"main.if", label %"main.endif"
main.if:
  %".19" = alloca [10 x i8]
  store [10 x i8] c"1_Always \00", [10 x i8]* %".19"
  %".21" = getelementptr [10 x i8], [10 x i8]* %".19", i32 0, i32 0
  %".22" = call i32 (...) @"printf"(i8* %".21")
  br label %"main.endif"
main.endif:
  %".24" = load i32, i32* %".6"
  %".25" = load i32, i32* %".8"
  %".26" = icmp sgt i32 %".24", %".25"
  br i1 %".26", label %"main.endif.if", label %"main.endif.endif"
main.endif.if:
  %".28" = alloca [7 x i8]
  store [7 x i8] c"Never \00", [7 x i8]* %".28"
  %".30" = getelementptr [7 x i8], [7 x i8]* %".28", i32 0, i32 0
  %".31" = call i32 (...) @"printf"(i8* %".30")
  br label %"main.endif.endif"
main.endif.endif:
  %".33" = load i32, i32* %".6"
  %".34" = load i32, i32* %".8"
  %".35" = icmp eq i32 %".33", %".34"
  br i1 %".35", label %"main.endif.endif.if", label %"main.endif.endif.endif"
main.endif.endif.if:
  %".37" = alloca [10 x i8]
  store [10 x i8] c"3_Always \00", [10 x i8]* %".37"
  %".39" = getelementptr [10 x i8], [10 x i8]* %".37", i32 0, i32 0
  %".40" = call i32 (...) @"printf"(i8* %".39")
  br label %"main.endif.endif.endif"
main.endif.endif.endif:
  %".42" = load i32, i32* %".6"
  %".43" = load i32, i32* %".4"
  %".44" = icmp ne i32 %".42", %".43"
  br i1 %".44", label %"main.endif.endif.endif.if", label %"main.endif.endif.endif.endif"
main.endif.endif.endif.if:
  %".46" = alloca [10 x i8]
  store [10 x i8] c"4_Always \00", [10 x i8]* %".46"
  %".48" = getelementptr [10 x i8], [10 x i8]* %".46", i32 0, i32 0
  %".49" = call i32 (...) @"printf"(i8* %".48")
  br label %"main.endif.endif.endif.endif"
main.endif.endif.endif.endif:
  ret i32 0
}

declare i32 @"printf"(...)
