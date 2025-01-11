top:
Cls
Screen 2

Locate 3, 25
Print "M"

Locate 3, 35
Print "E"

Locate 3, 45
Print "N"

Locate 3, 55
Print "U"

Line (10, 1)-(628, 1)
Line (10, 1)-(10, 628)
Line (10, 628)-(628, 628)
Line (628, 628)-(628, 1)

Locate 7, 30
Print "CHOOSE YOUR PROGAM"

Locate 8, 30
Print "1. Basic Programs"

Locate 9, 30
Print "2. Conditional Programs"

Locate 10, 30
Print "3. Iteration Control Structure"

Locate 11, 30
Print "4. Series Generation"

Locate 12, 30
Print "5. Library Functions"

Locate 13, 30
Print "6. Exit"

Locate 17, 30
Input "Please enter any option(1-6)"; n

Sleep 1

Cls
If n = 1 Then
    Print "1.Basic Programming"
    Print
    Print "a. To display the area and perimeter of the rectangle."
    Print
    Sleep 1
    Print "b. To enter any number and display its square root and cube root."
    Print
    Sleep 1
    Print "c. To accept in Celcius from the user and convert into Fahrenheit."
    Print
    Sleep 1
    Print "d. To calculate the area of the triangle by entering sides of a triangle."

    Input "Choose any option(a-d)"; a$
    a$ = LCase$(a$)
    Cls
    Select Case (a$)


        Case "a"
            Print "a. Calculate area and perimeter of a rectangle"
            Print
            Input "Enter the length of the rectangle: "; l
            Input "Enter the breadth of the rectangle: "; b

            a = l * b
            p = 2 * (l + b)
            Sleep 1

            Print "Area of the rectangle: "; a
            Print "Perimeter of the rectangle: "; p


        Case "b"
            Print "b. Calculate square root and cube root of a number"
            Print
            Input "Enter a number: "; n

            s = Sqr(n)
            c = n ^ (1 / 3)
            Sleep 1

            Print "Square root of the number: "; s
            Print "Cube root of the number: "; c


        Case "c"
            Print "c. Convert Celsius to Fahrenheit"
            Print
            Input "Enter temperature in Celsius: "; c

            f = (c * 9 / 5) + 32
            Sleep 1

            Print "Temperature in Fahrenheit: "; f


        Case "d"
            Print "d. Calculate the area of a triangle"
            Print
            Input "Enter the three sides of a triangle"; a, b, c

            s = (a + b + c) / 2
            a = Sqr(s * (s + -a) * (s - b) * (s - c))
            Sleep 1

            Print "Area of the triangle: "; a


    End Select
    a$ = Input$(1)
    GoTo top

ElseIf n = 2 Then
    Print "2.Conditional Statement"
    Print
    Print "a. To enter any number and check if it is even or odd."
    Print
    Sleep 1
    Print "b. To enter any number and print it is positive, negative or neutral."
    Print
    Sleep 1
    Print "c. To enter a number and check if it is divisible by 3 and 5 or not."
    Print
    Sleep 1
    Print "d. To enter three angles and check if it will form a triangle or not."
    Print
    Sleep 1
    Print "e. To enter any three numbers and display the smallest among the three numbers."
    Print
    Sleep 1
    Print "f. To enter a number and check if it is prime or composite."
    Print
    Input "Choose any option(a-f)"; b$
    b$ = LCase$(b$)
    Select Case (b$)


        Case "a"
            Print "a. To check if a number is even or odd"
            Print
            Input "Enter a number: "; n
            If n Mod 2 = 0 Then
                Print "The number is even."
            Else
                Print "The number is odd."
            End If


        Case "b"
            Print "b. To determine whether a number is positive, negative, or neutral"
            Print
            Input "Enter a number: "; n
            If n > 0 Then
                Print "The number is positive."
            ElseIf n < 0 Then
                Print "The number is negative."
            Else
                Print "The number is zero/neutral."
            End If


        Case "c"
            Print "c. To check if a number is divisible by 3 and 5"
            Print
            Input "Enter a number: "; n
            If (number Mod 3 = 0) And (number Mod 5 = 0) Then
                Print "The number is divisible by both 3 and 5."
            Else
                Print "The number is not divisible by both 3 and 5."
            End If


        Case "d"
            Print "d. To input three angles and check if it will form a triangle"
            Print
            Cls
            Input "Enter the angles"; a, b, c
            If a + b + c = 180 Then
                Print "It will form a triangle"
            Else
                Print "It will not form a triangle"
            End If


        Case "e"
            Print "e. To find the smallest among three numbers"
            Print
            Cls
            Input "Enter any three numbers"; a, b, c
            If a < b And a < c Then
                Print a; "is the smallest number among the three"
            ElseIf b < a And b < c Then
                Print b; "is the smallest number among the three"
            ElseIf c < a And c < b Then
                Print c; "is the smallest number among the three"
            Else
                Print "Invalid/enter different numbers"
            End If


        Case "f"
            Print "f. To check if a number is prime or composite"
            Print
            Cls
            Input "Enter a number: "; n
            If n Mod k = 0 Then
                c = c + 1
            End If
            If c > 2 Then
                Print "Composite number"
            ElseIf c = 2 Then
                Print "Prime number"
            Else
                Print "Neither prime nor composite"
            End If


    End Select
    a$ = Input$(1)
    GoTo top


End If

