from flet import *
 
hovering = False

def home(page):
    page.padding=1
    page.bgcolor="white"
    page.scroll="auto"
    page.update()
    def go_to_lessons_page(e):
        page.controls.clear()
        lessons(page)
        page.update()
    def animate_buttons(e):
        global hovering
        if e.data == 'true' and not hovering:

            e.control.scale = 1.2
            e.control.bgcolor ="#6B0000"
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale=1
            e.control.bgcolor="#8A0000"
            hovering = False
        page.update()
    # HEADER
    first_photo = Container(
        content=Image(
            src="https://i.postimg.cc/hvp8qwv1/BAC-DZ-20260802-200511-0000.png",
            fit=ImageFit.COVER,
            
        ),
        padding=10,
        margin=0,
        alignment = alignment.top_center
    )

    button_of_action = Stack(
            controls=[
                Container(
                    content = Row(controls=[ElevatedButton(bgcolor='#8A0000',color='white',width=100,height=60,on_hover=animate_buttons,content=Container(content=Text('home',size=20,text_align=TextAlign.CENTER))),
                        ElevatedButton(bgcolor='#8A0000',color="white",width=100,height=60,on_hover=animate_buttons,content=Container(content=Text('about us',size=20,text_align=TextAlign.CENTER))),
                        ElevatedButton(bgcolor='#8A0000',color="white",width=100,height=60,on_hover=animate_buttons,content=Container(content=Text('dawnold App',size=20,text_align=TextAlign.CENTER))),
                        ElevatedButton(bgcolor='#8A0000',color="white",width=100,height=60,on_hover=animate_buttons,content=Container(content=Text('give feed back',size=20,text_align=TextAlign.CENTER))),],
                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        spacing=1

                        ),

                    
                    alignment=alignment.center,
                    bgcolor='#8A0000'

                )   
            ],

    )

    first_frame = Row([
        Container(
            content=Column([
                Text('lessons and summaries',color='black',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('we offert a complet and well-structured lessons for all BAC subject ',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#8A0000',on_hover=animate_buttons,on_click=go_to_lessons_page,content=Container(content=Text('lessons and summaries',size=20,text_align=TextAlign.CENTER)))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=0)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    second_frame = Row([
        Container(
            content=Column([
                Text('youtube channel',color='black',weight='bold',size=33),
                Text('all what you need from channel for all subject ',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(text='youtube channel',width=200,height=60,color='white',bgcolor='#8A0000',style=ButtonStyle(text_style=TextStyle(size=20)),on_hover=animate_buttons)


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    therd_frame = Row([
        Container(
            content=Column([
                Text('previous BAC subject ',color='black',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('We offert all past BAc test for more trainig',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#8A0000',on_hover=animate_buttons,content=Container(content=Text('previous BAC subject',size=20,text_align=TextAlign.CENTER)))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    fourth_frame = Row([
        Container(
            content=Column([
                Text('subject of the school year',color='black',weight='bold',size=33,text_align=TextAlign.CENTER),
                Text('we also offert the school year test ',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#8A0000',on_hover=animate_buttons,content=Container(content=Text('subject of the school year',size=20,text_align=TextAlign.CENTER)))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )


    fifth_frame = Row([
        Container(
            content=Column([
                Text('Ask AI',color='black',weight='bold',size=33),
                Text('if you are confuse ask AI for more information',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(width=200,height=60,color='white',bgcolor='#8A0000',on_hover=animate_buttons,content=Container(content=Text('ask AI',size=20,text_align=TextAlign.CENTER)))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )

    six_frame = Row([
        Container(
            content=Column([
                Text('ZOOM cours ',color='black',weight='bold',size=33),
                Text('COMMING SOON',color='black',size=20,text_align=TextAlign.CENTER),
                ElevatedButton(text='COMMING SOON',width=200,height=60,color='white',bgcolor='#8A0000',style=ButtonStyle(text_style=TextStyle(size=20)))


                ],
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER

                ),
            border=border.all(3,'black'),
            padding=10,
            width=300,
            height=400,
            alignment = alignment.center,
            margin = margin.only(top=20)
            )
            


        ],
        alignment= MainAxisAlignment.CENTER
        )
    
    page.add(button_of_action)
    page.add(first_photo)
    page.add(first_frame)
    page.add(second_frame)
    page.add(therd_frame)
    page.add(fourth_frame)
    page.add(fifth_frame)
    page.update()