declare mistake()
declare order_placed()

declare homepage()
declare login()
declare sign_up()
declare products()
declare normal()
declare admin()

declare pre()
declare orders()
declare pre_astroball()
declare pre_astroball_orders()
declare pre_peanut_butter_scooper()
declare pre_peanut_butter_scooper_orders()
declare pre_elementary_complex_analysis()
declare pre_elementary_complex_analysis_orders()

declare coming_soon()
declare cs_jbl_headphones()

declare auction()
declare auction_midas_staff()
declare auction_picasso_painting()
declare auction_van_gogh()

declare pets()
declare pets_dog()
declare pets_dog_orders()
declare pets_cat()
declare pets_cat_orders()

declare books()
declare books_mathematics()
declare books_math_real_analysis()
declare books_math_real_analysis_orders()
declare books_math_complex_analysis()
declare books_math_complex_analysis_orders()
declare books_math_calculus_all()
declare books_math_calculus_all_orders()
declare books_math_algebra_all()
declare books_cs()
declare books_cs_python()
declare books_cs_python_orders()

Cls

Screen 13
Call homepage

End
Sub order_placed ()
    Cls
    Color 2
    Locate 10, 15
    Print "ORDER PLACED!"
    Sleep 1
    Cls
    Color 15
    Locate 10, 15
    Print "Attempting to get you back to the home page."
    Sleep 1
    Cls
    Locate 10, 15
    Print "Attempting to get you back to the home page.."
    Sleep 1
    Cls
    Locate 10, 15
    Print "Attempting to get you back to the home page..."
    Sleep 1
    Cls
    Call homepage
End Sub
Sub mistake ()
    Cls
    Locate 10, 18
    Color 4
    Print "ERROR!"
    Print "It appears you have made an error."
    Print "Attempting to get you back."
    Sleep 1
    Cls
    Locate 10, 18
    Color 4
    Print "ERROR!"
    Print "It appears you have made an error.."
    Print "Attempting to get you back.."
    Sleep 1
    Cls
    Locate 10, 18

    Color 4
    Print "ERROR!"
    Print "It appears you have made an error..."
    Print "Attempting to get you back..."
    Sleep 1
    Cls
    Locate 10, 15
    Color 2
    Print "SUCCESSFUL!"
    Sleep 1
    Cls
    Call homepage

End Sub
Sub homepage ()
    Color 15
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "HOME PAGE"
    Line (0, 35)-(318, 35)
    Locate 8, 18
    Print "ADMIN"
    Locate 12, 15
    Print "NORMAL USER"
    Locate 20, 6
    Input "Which user are you"; admin_or_normal$
    If LCase$(Left$(admin_or_normal$, 1)) = "n" Then
        Cls
        Call normal
    ElseIf LCase$(Left$(admin_or_normal$, 1)) = "a" Then
        Cls
        Call admin
    Else
        Call mistake
    End If

End Sub
Sub normal ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "NORMAL USER"
    Line (0, 35)-(318, 35)
    Locate 8, 16
    Print "LOG IN"
    Locate 12, 16
    Print "SIGN UP ON OUR WEBSITE"
    Locate 20, 6
    Input "What do you want to do"; normal_login_or_signup$
    If LCase$(Left$(normal_login_or_signup$, 1)) = "l" Then
        Cls
        Call login
    Else
        Call mistake
    End If
End Sub
Sub admin ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "ADMIN"
    Line (0, 35)-(318, 35)
    Locate 8, 10
    Input "ENTER PASSWORD"; admin_pass$
    If admin_pass$ = "hellojustsayingiamontheleaderboardsofprojecteulernepal" or admin_pass$ = "dipen" Then
        Cls
        Call orders
    Else
        Call mistake
    End If
End Sub
Sub login ()
    Open "users.txt" For Input As #1
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "LOG IN"
    Line (0, 35)-(318, 35)
    Locate 8, 10
    Input "ENTER YOUR KEY"; login_key
    While Not EOF(1):
        Input #1, n, n$, lk
        If lk = login_key Then
            Cls
            Call products
        Else
            a = a + 1
        End If
    Wend

End Sub
Sub sign_up ()
    Open "users.txt" For Input As #1
    While Not EOF(1):
        Input #1, n, n$, lk
        number = n
    Wend
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "SIGN UP"
    Line (0, 35)-(318, 35)
    Locate 8, 16
    Input "Please enter your name"; n$
    Input "Please enter your new login key"; lk
    number = number + 1
    Close
    Open "users.txt" For Output As #1
    Write #1, number, n$, lk
    Sleep 1
    Cls
    Call login
End Sub
Sub products ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "PRODUCTS"
    Line (0, 35)-(318, 35)
    Locate 7, 16
    Print "PRE ORDERS"
    Locate 9, 16
    Print "COMING SOON"
    Locate 11, 16
    Print "AUCTION"
    Locate 13, 16
    Print "CUSTOMER TO CUSTOMER"
    Locate 15, 16
    Print "PETS"
    Locate 17, 16
    Print "BOOKS"
    Locate 20, 10
    Input "Where do you want to go"; product$
    If LCase$(Left$(product$, 3)) = "pre" Then
        Cls
        Call pre
    ElseIf LCase$(Left$(product$, 2)) = "co" Then
        Cls
        Call coming_soon
    ElseIf LCase$(Left$(product$, 1)) = "a" Then
        Cls
        Call auction
    ElseIf LCase$(Left$(product$, 1)) = "p" Then
        Cls
        Call pets
    ElseIf LCase$(Left$(product$, 1)) = "b" Then
        Cls
        Call books
    Else
        Call mistake
    End If
End Sub
Sub pre ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "PRE ORDERS"
    Line (0, 35)-(318, 35)
    Locate 7, 16
    Print "ASTROBALL"
    Locate 9, 16
    Print "PEANUT BUTTER SCOOPER"
    Locate 11, 16
    Print "MRBEAST SHIRT"
    Locate 13, 16
    Print "RUBY DRILL"
    Locate 15, 16
    Print "ELEMENTARY COMPLEX ANALYSIS"
    Locate 17, 16
    Input "Which product do you want to see"; pre_order$
    If LCase$(Left$(pre_order$, 1)) = "a" Then
        Cls
        Call pre_astroball
    ElseIf LCase$(Left$(pre_order$, 1)) = "p" Then
        Cls
        Call pre_peanut_butter_scooper
    ElseIf LCase$(Left$(pre_order$, 1)) = "e" Then
        Cls
        Call pre_elementary_complex_analysis
    Else
        Call mistake
    End If
End Sub
Sub orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "ORDERS"
    Line (0, 35)-(318, 35)
    Locate 7, 16
    Print "ASTROBALL ORDERS"
    Locate 9, 16
    Print "PEANUT BUTTER SCOOPER ORDERS"
    Locate 11, 16
    Print "MRBEAST SHIRT ORDERS"
    Locate 13, 16
    Print "RUBY DRILL ORDERS"
    Locate 15, 16
    Print "ELEMENTARY COMPLEX ANALYSIS ORDERS"
    Locate 17, 16
    Input "Which product do you want to see"; pre_order$
    If LCase$(Left$(pre_order$, 1)) = "a" Then
        Cls
        Call pre_astroball_orders
    ElseIf LCase$(Left$(pre_order$, 1)) = "p" Then
        Cls
        Call pre_peanut_butter_scooper_orders
    ElseIf LCase$(Left$(pre_order$, 1)) = "e" Then
        Cls
        Call pre_elementary_complex_analysis_orders
    Else
        Call mistake
    End If

End Sub
Sub pre_astroball ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "ASTROBALL"
    Locate 8, 10
    Print "A very fun ball that automatically goes back into your hand after you throw it down! It is very bouncy ball so it is to be noted that any injuries caused by this will not be our fault."
    Locate 20, 19
    Input "Do you want to preorder this item"; pre_astro$
    If LCase$(Left$(pre_astro$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If
End Sub
Sub pre_astroball_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Joseph Stalin"
    Locate 8, 15
    'Product Name
    Print "ASTROBALL"
    Locate 8, 27
    'Remarks
    Print "-"
    Locate 8, 32
    'Date
    Print "11/4/1922"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "JSchlatt"
    Locate 11, 15
    'Product Name
    Print "ASTROBALL"
    Locate 11, 27
    'Remarks
    Print "-"
    Locate 11, 32
    'Date
    Print "9/11/1999"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Travis Scott"
    Locate 13, 15
    'Product Name
    Print "ASTROBALL"
    Locate 13, 27
    'Remarks
    Print "Scam"
    Locate 13, 32
    'Date
    Print "10/3/2021"

End Sub
Sub pre_peanut_butter_scooper ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "PEANUT BUTTER SCOOPER"
    Locate 8, 10
    Print "A very not useless item that will help you scoop up peanut butter and mix it in if it is very oily and old."
    Locate 20, 19
    Input "Do you want to preorder this item"; pre_pb$
    If LCase$(Left$(pre_pb$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If

End Sub
Sub pre_peanut_butter_scooper_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Metro"
    Locate 8, 15
    'Product Name
    Print "PB Scooper"
    Locate 8, 27
    'Remarks
    Print "-"
    Locate 8, 32
    'Date
    Print "11/4/2024"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Future"
    Locate 11, 15
    'Product Name
    Print "PB Scooper"
    Locate 11, 27
    'Remarks
    Print "Nice"
    Locate 11, 32
    'Date
    Print "10/4/2014"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Prakrit"
    Locate 13, 15
    'Product Name
    Print "PB Scooper"
    Locate 13, 27
    'Remarks
    Print "-"
    Locate 13, 32
    'Date
    Print "11/4/2021"

    Locate 15, 2
    Print "4"
    Locate 15, 4
    'Name
    Print "Drake"
    Locate 15, 15
    'Product Name
    Print "PB Scooper"
    Locate 15, 27
    'Remarks
    Print "odep"
    Locate 15, 32
    'Date
    Print "11/29/2019"


End Sub
Sub pre_elementary_complex_analysis ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "ELEMENTARY COMPLEX ANALYSIS"
    Locate 8, 10
    Print "A very useful book for someone who is just starting out complex analysis. NOTE THAT THIS IS NOT FOR TOTAL BEGINNERS."
    Locate 20, 19
    Input "Do you want to preorder this item"; pre_eca$
    If LCase$(Left$(pre_eca$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If

End Sub
Sub pre_elementary_complex_analysis_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Dave"
    Locate 8, 15
    'Product Name
    Print "Complex"
    Locate 8, 27
    'Remarks
    Print "-"
    Locate 8, 32
    'Date
    Print "11/4/2023"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Knee Grow"
    Locate 11, 15
    'Product Name
    Print "Complex"
    Locate 11, 27
    'Remarks
    Print "Nice"
    Locate 11, 32
    'Date
    Print "11/4/2024"


End Sub
Sub coming_soon ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "COMING SOON"
    Line (0, 35)-(318, 35)
    Locate 7, 16
    Print "JBL HEADPHONES"
    Input "Which product do you want to see"; coming$
    If LCase$(Left$(coming$, 1)) = "j" Then
        Cls
        Call cs_jbl_headphones
    Else
        Cls
        Call mistake
    End If
End Sub
Sub cs_jbl_headphones ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "JBL HEADPHONES"
    Locate 8, 10
    Print "Up your listening game with these new JBL Headphones! With never-seen-before technology at it's hands, it will make your listening a lot more nicer with it's noise-cancelling features, AI built-in assistant, and hand-free calls with the buttons on the hide of the headphones."
End Sub
Sub auction ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "AUCTION"
    Line (0, 35)-(318, 35)
    Locate 7, 16
    Print "MIDAS STAFF"
    Locate 9, 16
    Print "MIDAS' SWORD"
    Locate 11, 16
    Print "PICASSO PAINTING"
    Locate 13, 16
    Print "VAN GOGH PAINTING"
    Locate 15, 16
    Print "LOST MOZART SONG"
    Locate 19, 16
    Input "Which product do you want to see"; auction_input$
    If LCase$(Right$(auction_input$, 1)) = "f" Then
        Cls
        Call auction_midas_staff
    ElseIf LCase$(Left$(auction_input$, 1)) = "p" Then
        Cls
        Call auction_picasso_painting
    ElseIf LCase$(Left$(auction_input$, 1)) = "v" Then
        Cls
        Call auction_van_gogh
    Else
        Call mistake
    End If
End Sub
Sub auction_midas_staff ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "MIDAS STAFF"
    Locate 8, 10
    Print "A magical staff. It is said that, when used properly, a huge rain of gold appears. Can be used to defeat any person easily."
    Locate 20, 19
    Input "How much do you want to auction"; auction_amount
    Cls
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 10, 15
    Print "Thank you for your auction!"
    Sleep 1
    Cls
    Call homepage


End Sub
Sub auction_picasso_painting ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "PICASSO PAINTING"
    Locate 8, 10
    Print "A lost painting found, made by Picasso. Note that this was made in his childhood years, making this painting even more valuable."
    Locate 20, 19
    Input "How much do you want to auction"; auction_amount
    Cls
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 10, 15
    Print "Thank you for your auction!"
    Sleep 1
    Cls
    Call homepage

End Sub
Sub auction_van_gogh ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "VAN GOGH EAR"
    Locate 8, 10
    Print "The legendary Van Gogh's ear, that he cut off because his wife wanted to do it. Questionable, but it is still a very good antique for historians."
    Locate 20, 19
    Input "How much do you want to auction"; auction_amount
    Cls
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 10, 15
    Print "Thank you for your auction!"
    Sleep 1
    Cls
    Call homepage


End Sub
Sub pets ()
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "PETS"
    Line (0, 35)-(318, 35)
    Locate 7, 16
    Print "DOG"
    Locate 9, 16
    Print "CAT"
    Locate 19, 16
    Input "Which pet do you want to see"; pet$
    If LCase$(Right$(pet$, 1)) = "d" Then
        Cls
        Call pets_dog
    ElseIf LCase$(Right$(pet$, 1)) = "c" Then
        Cls
        Call pets_cat
    Else
        Call mistake
    End If
End Sub
Sub pets_dog ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "PET DOG"
    Locate 8, 10
    Print "It is said that a dog is a man's best friend. We have the best dogs in the whole world! Get your dog for you or your kids now."
    Locate 20, 19
    Input "Do you want to order this item"; dog$
    If LCase$(Left$(dog$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If

End Sub
Sub pets_dog_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Katlyn"
    Locate 8, 15
    'Product Name
    Print "Dog"
    Locate 8, 27
    'Remarks
    Print "Cute"
    Locate 8, 32
    'Date
    Print "11/25/2021"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "David"
    Locate 11, 15
    'Product Name
    Print "Dog"
    Locate 11, 27
    'Remarks
    Print "Woohoo!"
    Locate 11, 32
    'Date
    Print "6/3/2020"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Blueface"
    Locate 13, 15
    'Product Name
    Print "Dog"
    Locate 13, 27
    'Remarks
    Print "-"
    Locate 13, 32
    'Date
    Print "11/4/2024"

    Locate 15, 2
    Print "4"
    Locate 15, 4
    'Name
    Print "Anonymous"
    Locate 15, 15
    'Product Name
    Print "Dog"
    Locate 15, 27
    'Remarks
    Print "-"
    Locate 15, 32
    'Date
    Print "11/4/2024"

    Locate 18, 2
    Print "5"
    Locate 18, 4
    'Name
    Print "Anonymous"
    Locate 18, 15
    'Product Name
    Print "Dog"
    Locate 18, 27
    'Remarks
    Print "-"
    Locate 18, 32
    'Date
    Print "11/4/2024"

    Locate 21, 2
    Print "6"
    Locate 21, 4
    'Name
    Print "Jeremy"
    Locate 21, 15
    'Product Name
    Print "ASTROBALL"
    Locate 21, 27
    'Remarks
    Print "omg"
    Locate 21, 32
    'Date
    Print "11/4/1924"



End Sub
Sub pets_cat ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "PET CAT"
    Locate 8, 10
    Print "Cats are a dog's enemy, as seen in the show Oggy and the Cockroaches. But, if you train them, the cat can be friendly with anyone. Get your cat today."
    Locate 20, 19
    Input "Do you want to order this item"; cat$
    If LCase$(Left$(cat$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If


End Sub
Sub pets_cat_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Sameeza"
    Locate 8, 15
    'Product Name
    Print "Cat"
    Locate 8, 27
    'Remarks
    Print "cat"
    Locate 8, 32
    'Date
    Print "11/4/2023"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Sarthak"
    Locate 11, 15
    'Product Name
    Print "Cat"
    Locate 11, 27
    'Remarks
    Print "-"
    Locate 11, 32
    'Date
    Print "7/1/2022"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Kushal"
    Locate 13, 15
    'Product Name
    Print "Cat"
    Locate 13, 27
    'Remarks
    Print "meow"
    Locate 13, 32
    'Date
    Print "11/4/2022"

    Locate 15, 2
    Print "4"
    Locate 15, 4
    'Name
    Print "Dipen"
    Locate 15, 15
    'Product Name
    Print "Cat"
    Locate 15, 27
    'Remarks
    Print "Dipen"
    Locate 15, 32
    'Date
    Print "11/4/2024"

    Locate 18, 2
    Print "5"
    Locate 18, 4
    'Name
    Print "CatLover20"
    Locate 18, 15
    'Product Name
    Print "Cat"
    Locate 18, 27
    'Remarks
    Print "-"
    Locate 18, 32
    'Date
    Print "4/4/2021"

    Locate 21, 2
    Print "6"
    Locate 21, 4
    'Name
    Print "CatLover21"
    Locate 21, 15
    'Product Name
    Print "Cat"
    Locate 21, 27
    'Remarks
    Print "-"
    Locate 21, 32
    'Date
    Print "4/4/2024"



End Sub
Sub books ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "BOOKS"
    Line (0, 35)-(318, 35)
    Locate 11, 16
    Print "MATHEMATICS"
    Locate 15, 16
    Print "COMPUTER SCIENCE"
    Locate 19, 16
    Input "Which product do you want to see"; book$
    If LCase$(Left$(book$, 1)) = "m" Then
        Cls
        Call books_mathematics
    ElseIf LCase$(Left$(book$, 2)) = "c" Then
        Cls
        Call books_cs
    Else
        Call mistake
    End If

End Sub
Sub books_mathematics ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "MATHEMATICS"
    Line (0, 35)-(318, 35)
    Locate 11, 16
    Print "REAL ANALYSIS"
    Locate 13, 16
    Print "COMPLEX ANALYSIS"
    Locate 15, 16
    Print "CALCULUS ALL"
    Locate 17, 16
    Print "ALGEBRA ALL"
    Locate 19, 16
    Input "Which product do you want to see"; math$
    If LCase$(Left$(math$, 1)) = "r" Then
        Cls
        Call books_math_real_analysis
    ElseIf LCase$(Left$(math$, 2)) = "a" Then
        Cls
        Call books_math_calculus_all
    ElseIf LCase$(Left$(math$, 1)) = "a" Then
        Cls
        Call books_math_algebra_all
    ElseIf LCase$(Left$(math$, 2)) = "o" Then
        Cls
        Call books_math_complex_analysis
    Else
        Call mistake
    End If

End Sub
Sub books_math_real_analysis ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "REAL ANALYSIS"
    Locate 8, 10
    Print "Open your eyes with this real analysis book. It is best for BSc. Mathematics Students."
    Locate 20, 19
    Input "Do you want to order this item"; ra$
    If LCase$(Left$(ra$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If


End Sub
Sub books_math_real_analysis_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Prakrit"
    Locate 8, 15
    'Product Name
    Print "Analysis"
    Locate 8, 27
    'Remarks
    Print "Love"
    Locate 8, 32
    'Date
    Print "11/4/2024"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Euler"
    Locate 11, 15
    'Product Name
    Print "Analysis"
    Locate 11, 27
    'Remarks
    Print "-"
    Locate 11, 32
    'Date
    Print "11/4/1729"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Bernoulli"
    Locate 13, 15
    'Product Name
    Print "Analysis"
    Locate 13, 27
    'Remarks
    Print "-"
    Locate 13, 32
    'Date
    Print "11/4/2021"

    Locate 15, 2
    Print "4"
    Locate 15, 4
    'Name
    Print "Fermat"
    Locate 15, 15
    'Product Name
    Print "Analysis"
    Locate 15, 27
    'Remarks
    Print "-"
    Locate 15, 32
    'Date
    Print "11/15/2021"

    Locate 18, 2
    Print "5"
    Locate 18, 4
    'Name
    Print "Descartes"
    Locate 18, 15
    'Product Name
    Print "Analysis"
    Locate 18, 27
    'Remarks
    Print "-"
    Locate 18, 32
    'Date
    Print "5/7/2019"

    Locate 21, 2
    Print "6"
    Locate 21, 4
    'Name
    Print "Turing"
    Locate 21, 15
    'Product Name
    Print "Analysis"
    Locate 21, 27
    'Remarks
    Print "-"
    Locate 21, 32
    'Date
    Print "11/4/2024"



End Sub
Sub books_math_complex_analysis ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "COMPLEX ANALYSIS"
    Locate 8, 10
    Print "Oh, so real analysis wasn't enough? Torture yourself with this absolutely MARVELOUS Complex Analysis book. It contains all of complex analysis, so it is really, REALLY not recommended for people who have not messed around with math."
    Locate 20, 19
    Input "Do you want to order this item"; ca$
    If LCase$(Left$(ca$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If


End Sub
Sub books_math_complex_analysis_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Prakrit"
    Locate 8, 15
    'Product Name
    Print "Complex"
    Locate 8, 27
    'Remarks
    Print "-"
    Locate 8, 32
    'Date
    Print "11/4/2024"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Goldbach"
    Locate 11, 15
    'Product Name
    Print "Complex"
    Locate 11, 27
    'Remarks
    Print "-"
    Locate 11, 32
    'Date
    Print "11/3/2017"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Gauss"
    Locate 13, 15
    'Product Name
    Print "Complex"
    Locate 13, 27
    'Remarks
    Print "-"
    Locate 13, 32
    'Date
    Print "1/1/2000"

    Locate 15, 2
    Print "4"
    Locate 15, 4
    'Name
    Print "Lagrange"
    Locate 15, 15
    'Product Name
    Print "Complex"
    Locate 15, 27
    'Remarks
    Print "-"
    Locate 15, 32
    'Date
    Print "5/7/2016"

    Locate 18, 2
    Print "5"
    Locate 18, 4
    'Name
    Print "Laplace"
    Locate 18, 15
    'Product Name
    Print "Complex"
    Locate 18, 27
    'Remarks
    Print "-"
    Locate 18, 32
    'Date
    Print "2/4/1999"

    Locate 21, 2
    Print "6"
    Locate 21, 4
    'Name
    Print "Fourier"
    Locate 21, 15
    'Product Name
    Print "Complex"
    Locate 21, 27
    'Remarks
    Print "-"
    Locate 21, 32
    'Date
    Print "4/5/2005"



End Sub
Sub books_math_calculus_all ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "CALCULUS"
    Locate 8, 10
    Print "Find out the wonders of calculus with this awesome book. It contains integration, differentiation, limits, series, basically everything that you need to know for calculus. Yes it does contain vector calculus if you hate yourself that much."
    Locate 20, 19
    Input "Do you want to order this item"; cal$
    If LCase$(Left$(cal$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If


End Sub
Sub books_math_calculus_all_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "Prakrit"
    Locate 8, 15
    'Product Name
    Print "Calculus"
    Locate 8, 27
    'Remarks
    Print "-"
    Locate 8, 32
    'Date
    Print "10/4/2023"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Newton"
    Locate 11, 15
    'Product Name
    Print "Calculus"
    Locate 11, 27
    'Remarks
    Print "Wait.."
    Locate 11, 32
    'Date
    Print "11/4/1694"

    Locate 13, 2
    Print "3"
    Locate 13, 4
    'Name
    Print "Leibniz"
    Locate 13, 15
    'Product Name
    Print "Calculus"
    Locate 13, 27
    'Remarks
    Print "-"
    Locate 13, 32
    'Date
    Print "11/4/2021"

    Locate 15, 2
    Print "4"
    Locate 15, 4
    'Name
    Print "Nerd"
    Locate 15, 15
    'Product Name
    Print "Calculus"
    Locate 15, 27
    'Remarks
    Print "Love"
    Locate 15, 32
    'Date
    Print "11/4/2024"

    Locate 18, 2
    Print "5"
    Locate 18, 4
    'Name
    Print "Niral"
    Locate 18, 15
    'Product Name
    Print "Calculus"
    Locate 18, 27
    'Remarks
    Print "-"
    Locate 18, 32
    'Date
    Print "12/11/2021"

    Locate 21, 2
    Print "6"
    Locate 21, 4
    'Name
    Print "Sambeed"
    Locate 21, 15
    'Product Name
    Print "Calculus"
    Locate 21, 27
    'Remarks
    Print "-"
    Locate 21, 32
    'Date
    Print "11/4/2021"



End Sub
Sub books_math_algebra_all ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "ALGEBRA"
    Locate 8, 10
    Print "Algebra is very simple. Fight me. Anyways, this book is one of the best for learning algebra. Very beginner-friendly."
    Locate 20, 19
    Input "Do you want to order this item"; alg$
    If LCase$(Left$(alg$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If


End Sub
Sub books_cs ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Locate 3, 16
    Print "COMPUTER SCIENCE"
    Line (0, 35)-(318, 35)
    Locate 15, 16
    Print "PYTHON"
    Locate 19, 16
    Input "Which product do you want to see(Theres really only one, do not mess this up)"; math$
    If LCase$(Left$(math$, 1)) = "p" Then
        Cls
        Call books_cs_python
    Else
        Cls
        Print "did you really mess that up..."
        Sleep 1
        Cls
        Print "I guess you found this 'easter egg' lol"
        Sleep 1
        Cls
        Print "shameless promotion time: I AM NUMBER 86 ON PrOBLEM 903 OF PROJECT EULER!!! I am also in the top 100 of nepal leaderboards, as of right now, number 62."
        Cls
        Sleep 1
        Print "alright bye bye"
        Sleep 1
        Cls
        Print "i said bye bye"
        Sleep 1
        Cls
        Print "you know what ill stop this, i need to finish everything else"
        Sleep 1
        Cls
        Print "just joking lol"
        Sleep 1
        Cls
        Print "ok for real this time"
        Sleep 1
        Cls
        Call mistake
    End If

End Sub
Sub books_cs_python ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Locate 3, 15
    Print "PYTHON"
    Locate 8, 10
    Print "No, this isnt the wrong section. If you're looking for a real python, go to some Indian black market. Anyways, this book is really great for people who want to learn python."
    Locate 20, 19
    Input "Do you want to order this item"; py$
    If LCase$(Left$(py$, 1)) = "y" Then
        Call order_placed
    Else
        Sleep 1
        Cls
        Locate 10, 15
        Print "Getting you to the home page..."
        Sleep 1
        Cls
        Call homepage
    End If


End Sub
Sub books_cs_python_orders ()
    Line (0, 0)-(318, 0)
    Line (0, 0)-(0, 180)
    Line (0, 180)-(318, 180)
    Line (318, 0)-(318, 180)
    Line (0, 40)-(318, 40)
    Line (20, 40)-(20, 180)
    Line (0, 50)-(318, 50)
    Line (0, 70)-(318, 70)
    Line (0, 90)-(318, 90)
    Line (0, 110)-(318, 110)
    Line (0, 130)-(318, 130)
    Line (0, 150)-(318, 150)
    Line (100, 40)-(100, 180)
    Line (200, 40)-(200, 180)
    Line (250, 40)-(250, 180)
    Locate 8, 2
    Print "1"
    Locate 8, 4
    'Name
    Print "David"
    Locate 8, 15
    'Product Name
    Print "Python"
    Locate 8, 27
    'Remarks
    Print "-"
    Locate 8, 32
    'Date
    Print "11/4/1984"
    Locate 11, 2
    Print "2"
    Locate 11, 4
    'Name
    Print "Bergcamp"
    Locate 11, 15
    'Product Name
    Print "Python"
    Locate 11, 27
    'Remarks
    Print "-"
    Locate 11, 32
    'Date
    Print "2/23/2004"

End Sub
