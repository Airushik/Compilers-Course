; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
main:
  %".2" = alloca [5 x i32]
  store [5 x i32] [i32 3, i32 1, i32 5, i32 6, i32 2], [5 x i32]* %".2"
  %".4" = load [5 x i32], [5 x i32]* %".2"
  %".5" = alloca i32
  store i32 5, i32* %".5"
  %".7" = alloca i32
  store i32 1, i32* %".7"
  %".9" = load i32, i32* %".5"
  br label %"main.loop_cond"
main.loop_cond:
  %".11" = load i32, i32* %".7"
  %".12" = icmp sgt i32 %".11", %".9"
  br i1 %".12", label %"main.loop_end", label %"main.loop_body"
main.loop_body:
  %".14" = alloca i32
  store i32 1, i32* %".14"
  %".16" = load i32, i32* %".5"
  %".17" = load i32, i32* %".7"
  %".18" = sub i32 %".16", %".17"
  br label %"main.loop_body.loop_cond"
main.loop_end:
  %".64" = alloca i32
  store i32 1, i32* %".64"
  %".66" = load i32, i32* %".5"
  br label %"main.loop_end.loop_cond"
main.loop_update:
  %".61" = add i32 %".11", 1
  store i32 %".61", i32* %".7"
  br label %"main.loop_cond"
main.loop_body.loop_cond:
  %".20" = load i32, i32* %".14"
  %".21" = icmp sgt i32 %".20", %".18"
  br i1 %".21", label %"main.loop_body.loop_end", label %"main.loop_body.loop_body"
main.loop_body.loop_body:
  %".23" = load i32, i32* %".14"
  %".24" = sub i32 %".23", 1
  %".25" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".24"
  %".26" = load i32, i32* %".25"
  %".27" = load i32, i32* %".14"
  %".28" = add i32 %".27", 1
  %".29" = sub i32 %".28", 1
  %".30" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".29"
  %".31" = load i32, i32* %".30"
  %".32" = icmp sgt i32 %".26", %".31"
  br i1 %".32", label %"main.loop_body.loop_body.if", label %"main.loop_body.loop_body.endif"
main.loop_body.loop_end:
  br label %"main.loop_update"
main.loop_body.loop_update:
  %".57" = add i32 %".20", 1
  store i32 %".57", i32* %".14"
  br label %"main.loop_body.loop_cond"
main.loop_body.loop_body.if:
  %".34" = load i32, i32* %".14"
  %".35" = sub i32 %".34", 1
  %".36" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".35"
  %".37" = load i32, i32* %".36"
  %".38" = alloca i32
  store i32 %".37", i32* %".38"
  %".40" = load i32, i32* %".14"
  %".41" = sub i32 %".40", 1
  %".42" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".41"
  %".43" = load i32, i32* %".14"
  %".44" = add i32 %".43", 1
  %".45" = sub i32 %".44", 1
  %".46" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".45"
  %".47" = load i32, i32* %".46"
  store i32 %".47", i32* %".42"
  %".49" = load i32, i32* %".14"
  %".50" = add i32 %".49", 1
  %".51" = sub i32 %".50", 1
  %".52" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".51"
  %".53" = load i32, i32* %".38"
  store i32 %".53", i32* %".52"
  br label %"main.loop_body.loop_body.endif"
main.loop_body.loop_body.endif:
  br label %"main.loop_body.loop_update"
main.loop_end.loop_cond:
  %".68" = load i32, i32* %".64"
  %".69" = icmp sgt i32 %".68", %".66"
  br i1 %".69", label %"main.loop_end.loop_end", label %"main.loop_end.loop_body"
main.loop_end.loop_body:
  %".71" = load i32, i32* %".64"
  %".72" = sub i32 %".71", 1
  %".73" = getelementptr [5 x i32], [5 x i32]* %".2", i32 0, i32 %".72"
  %".74" = load i32, i32* %".73"
  %".75" = alloca [4 x i8]
  store [4 x i8] c"%i \00", [4 x i8]* %".75"
  %".77" = getelementptr [4 x i8], [4 x i8]* %".75", i32 0, i32 0
  %".78" = call i32 (...) @"printf"(i8* %".77", i32 %".74")
  br label %"main.loop_end.loop_update"
main.loop_end.loop_end:
  ret i32 0
main.loop_end.loop_update:
  %".80" = add i32 %".68", 1
  store i32 %".80", i32* %".64"
  br label %"main.loop_end.loop_cond"
}

declare i32 @"printf"(...)
