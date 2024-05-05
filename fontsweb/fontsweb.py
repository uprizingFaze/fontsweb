from rxconfig import config
import reflex as rx

import fontsweb.styles.styles as styles


def navbar():
    return rx.hstack(
        rx.hstack(
            rx.image(src="/favicon.ico", width="2em"),
            rx.heading("Fonts Web", font_size="2em"),
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.content(
                rx.menu.item("Home"),
                rx.menu.item("Preview"),
                rx.menu.item("Sitio web"),
                rx.menu.item("Populares"),
            ),
            rx.color_mode_cond(
                light=rx.image(src="light.svg", height="4em"),
                dark=rx.image(src="dark.svg", height="4em"),
            ),
        ),
        position="fixed",
        top="0px",
        background_color="lightgray",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            padding_top="6em",
            max_width="60em",
        ),
        rx.text(
            "by uprizingFaze",
            class_name="text-xl text-neutral-700 ml-4 max-w-screen-xl mx-auto",
        ),
        rx.box(
            rx.text(
                "FONTS", class_name="text-9xl text-neutral-700 text-center font-bold"
            ),
            rx.text(
                "DESINGS", class_name="text-9xl text-neutral-700 text-center font-bold"
            ),
            direction="column",
            align_items="center",
            margin_y="4rem",
        ),
        rx.text(
            "Sitio web para previsualizar fuentes de texto de Google fonts, puedes ver las fuentes "
            "[aquí](https://fonts.google.com/) y copiar el nombre para ver la fuente en este sitio web.",
            class_name="text-xl text-neutral-700 ml-4",
            max_width="sm",
            text_align="center",
        ),
        rx.form(
            rx.input(
                type="text",
                placeholder="Nombre de la fuente por ejemplo: Sedan SC",
                value="",
                on_change="handleInputChange",
            ),
            rx.button("Ver", type="submit"),
            direction="row",
            align_items="center",
            space_x="2",
            margin_y="8rem",
            max_width="sm",
            on_submit="handleSubmit",
        ),
        rx.box(
            rx.box(
                rx.text("Typeface", class_name="text-neutral-700"),
                rx.text("fontFamily", class_name="text-3xl text-neutral-700 font-bold"),
                class_name="ring-1 ring-neutral-300 rounded-3xl p-4 col-span-2",
            ),
            rx.box(
                rx.text("Preview", class_name="text-neutral-700"),
                rx.text(
                    "Es através de los errores que realmente puedes crecer, hay que estar mal para poder lograr ser bueno.",
                    class_name="py-16 text-2xl text-neutral-700",
                ),
                class_name="ring-1 ring-neutral-300 rounded-3xl p-4 row-span-6",
            ),
            rx.box(
                rx.text("Aa", class_name="text-7xl text-white"),
                class_name="bgimg ring-1 ring-neutral-300 rounded-3xl col-span-2 row-span-6 justify-center items-center",
            ),
            rx.box(
                rx.text("License", class_name="text-neutral-700"),
                rx.text(
                    "Free for commercial use.",
                    class_name="py-6 text-2xl text-neutral-700",
                ),
                class_name="ring-1 ring-neutral-300 rounded-3xl p-4",
            ),
            direction="grid",
            grid_template_columns="repeat(3, 1fr)",
            gap="2",
            padding="2",
        ),
        rx.box(
            rx.box(
                class_name="ring-1 ring-black/30 dark:ring-white/30 rounded-3xl p-4",
                children=[
                    rx.text("Abc", class_name="color-secondary"),
                    rx.text(
                        "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn ñ Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz Ñ @ $ ¿? ¡! # % &",
                        class_name="text-2xl md:text-5xl",
                    ),
                ],
            ),
            class_name="px-2",
        ),
        # Numeros
        rx.box(
            rx.text("Numbers", class_name="text-7xl text-center py-24"),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("0 1 2 3 4 5 6 7 8 9", class_name="text-7xl ml-8"),
                rx.box(
                    rx.text("Size: 128px", class_name="text-xl"),
                    direction="column",
                ),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            direction="column",
        ),
        # Tamaños
        rx.box(
            rx.text("Size", class_name="text-7xl text-center py-24"),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-9xl", class_name="text-9xl ml-8"),
                rx.text("Size: 128px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-8xl", class_name="text-8xl ml-8"),
                rx.text("Size: 96px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-7xl", class_name="text-7xl ml-8"),
                rx.text("Size: 72px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-6xl", class_name="text-6xl ml-8"),
                rx.text("Size: 60px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-5xl", class_name="text-5xl ml-8"),
                rx.text("Size: 48px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-4xl", class_name="text-4xl ml-8"),
                rx.text("Size: 36px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-3xl", class_name="text-3xl ml-8"),
                rx.text("Size: 30px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-2xl", class_name="text-2xl ml-8"),
                rx.text("Size: 24px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            rx.box(
                rx.text("Text-xl", class_name="text-xl ml-8"),
                rx.text("Size: 20px", class_name="flex flex-col text-xl mr-8"),
                direction="row",
                justify_content="between",
            ),
            rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
            direction="column",
            id="size",
        ),
        # Estilo
        rx.box(
            rx.box(
                rx.text("Style", class_name="text-7xl text-center py-24"),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                rx.box(
                    rx.text("Italic", class_name="text-7xl ml-8 italic"),
                    direction="row",
                    justify_content="between",
                ),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                rx.box(
                    rx.text("Not italic", class_name="text-7xl ml-8 not-italic"),
                    direction="row",
                    justify_content="between",
                ),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                direction="column",
                id="family",
            ),
            rx.box(
                rx.text("Peso", class_name="text-7xl text-center py-24"),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                rx.box(
                    rx.text("Light", class_name="text-7xl ml-8 font-light"),
                    direction="row",
                    justify_content="between",
                ),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                rx.box(
                    rx.text("Medium", class_name="text-7xl ml-8 font-medium"),
                    direction="row",
                    justify_content="between",
                ),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                rx.box(
                    rx.text("Bold", class_name="text-7xl ml-8 font-bold"),
                    direction="row",
                    justify_content="between",
                ),
                rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
                direction="column",
                id="peso",
            ),
            direction="column",
        ),
        # Sitio web
        rx.box(
            rx.box(
                rx.text("Sitio web", class_name="text-7xl text-center"),
                padding_y="24",
            ),
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.box(class_name="h-3 w-3 bg-red-500 rounded-full mr-2"),
                            rx.box(
                                class_name="h-3 w-3 bg-yellow-500 rounded-full mr-2"
                            ),
                            rx.box(class_name="h-3 w-3 bg-green-500 rounded-full"),
                            direction="row",
                            align_items="center",
                            justify_content="start",
                            padding="2",
                            class_name="bg-white/10 rounded-t-xl",
                        ),
                        rx.box(
                            rx.box(
                                rx.box(
                                    rx.text(
                                        "by uprizingFaze",
                                        class_name="text-white dark:text-black",
                                    ),
                                    class_name="pt-8 pb-2",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.text(
                                            "Inicia tus web apps",
                                            class_name="text-5xl font-semibold text-white dark:text-black max-w-md",
                                        ),
                                        rx.text(
                                            "usando Reflex",
                                            class_name="text-5xl font-semibold text-white dark:text-black max-w-md",
                                        ),
                                        rx.text(
                                            "Crea Aplicaciones web mas rápido",
                                            class_name="mt-8 text-slate-300 dark:text-slate-700 max-w-md",
                                        ),
                                        rx.box(
                                            rx.text(
                                                "Comenzar ahora", class_name="mr-4 sm"
                                            ),
                                            rx.text("GitHub", class_name="ml-4 sm"),
                                            direction="row",
                                            class_name="mt-12",
                                        ),
                                        direction="column",
                                        class_name="mb-4 md:mb-0",
                                    ),
                                    rx.box(
                                        rx.image(
                                            src="reflex_dark.svg",
                                            width=300,
                                            height=300,
                                            alt="Reflex",
                                        ),
                                        class_name="px-2 pt-24",
                                    ),
                                    direction="row",
                                    class_name="mt-6 pl-4",
                                ),
                                class_name="ring-1 ring-white/30 dark:ring-white/30 rounded-b-3xl p-4 bg-black dark:bg-white",
                            ),
                            rx.box(
                                rx.box(
                                    rx.text("Fácil de Aprender", class_name="text-3xl"),
                                    rx.text(
                                        "Crea y comparte tu primera aplicación en minutos.",
                                        class_name="text-3xl",
                                    ),
                                    rx.hr(
                                        class_name="my-4 mx-5 border-black dark:border-white"
                                    ),
                                ),
                                rx.box(
                                    rx.text(
                                        "Fácil",
                                        class_name="bg-black text-white dark:bg-white dark:text-black text-xl rounded-xl p-2",
                                    ),
                                    rx.text(
                                        "Flexible",
                                        class_name="bg-black text-white dark:bg-white dark:text-black text-xl rounded-xl p-2",
                                    ),
                                    rx.text(
                                        "Codigo abierto",
                                        class_name="bg-black text-white dark:bg-white dark:text-black text-xl rounded-xl p-2",
                                    ),
                                    rx.text(
                                        "Ágil",
                                        class_name="bg-black text-white dark:bg-white dark:text-black text-xl rounded-xl p-2",
                                    ),
                                    direction="row",
                                    class_name="grid grid-cols-2 md:grid-cols-4 gap-4",
                                ),
                                rx.box(
                                    rx.box(
                                        rx.text(
                                            "Es momento de iniciar tu siguiente proyecto utilizando Reflex",
                                            class_name="text-3xl text-white dark:text-black px-12 pt-12",
                                        ),
                                        rx.box(
                                            rx.text(
                                                "Comenzar ahora", class_name="mr-4 sm"
                                            ),
                                            rx.text("GitHub", class_name="ml-4 sm"),
                                            direction="row",
                                            class_name="py-6",
                                        ),
                                        class_name="bg-black dark:bg-white rounded-t-3xl w-full",
                                    ),
                                    direction="column",
                                    align_items="center",
                                    justify_content="center",
                                    class_name="text-center pt-12 w-full",
                                ),
                                direction="column",
                                align_items="center",
                                justify_content="center",
                                class_name="text-center pt-12",
                            ),
                            direction="column",
                            class_name="px-1",
                        ),
                        class_name="ring-1 ring-black/30 dark:ring-white/30 rounded-t-xl",
                    ),
                    class_name="px-2",
                ),
                id="web-site",
            ),
            direction="column",
        ),
        # Fuentes populares
        rx.text("Fuentes populares", class_name="text-7xl text-center py-24"),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        rx.box(
            rx.box(
                rx.text("Crimson Text", class_name="text-7xl ml-8 font-normal"),
                rx.box(
                    rx.text("Font: Crimson Text"),
                    rx.text("Style: normal"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="crimson_Text.className",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        rx.box(
            rx.box(
                rx.text("Bebas Neue", class_name="text-7xl ml-8 font-bold"),
                rx.box(
                    rx.text("Font: Bebas Neue"),
                    rx.text("Style: Bolt"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="bebas_Neue.className",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        rx.box(
            rx.box(
                rx.text("Rock Salt", class_name="text-7xl ml-8"),
                rx.box(
                    rx.text("Font: Rock Salt"),
                    rx.text("Style: Normal"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="rock_Salt.className",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        rx.box(
            rx.box(
                rx.text("Dancing Script", class_name="text-7xl ml-8 font-semibold"),
                rx.box(
                    rx.text("Font: Dancing Script"),
                    rx.text("Style: SemiBolt"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="dancing_Script.className",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        rx.box(
            rx.box(
                rx.text("Sofia", class_name="text-7xl ml-8"),
                rx.box(
                    rx.text("Font: Sofia"),
                    rx.text("Style: Normal"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="sofia.className",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        rx.box(
            rx.box(
                rx.text("Eater", class_name="text-7xl ml-8 font-semibold"),
                rx.box(
                    rx.text("Font: Eater"),
                    rx.text("Style: SemiBolt"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="Eater.className",
        ),
        # Footer
        rx.box(
            rx.box(
                rx.box(
                    rx.text(
                        "by ",
                        rx.text(
                            "uprizingFaze", class_name="text-black dark:text-white"
                        ),
                        " proyecto para el ",
                        rx.text("Holamundo.day", class_name="Moure"),
                        " de MoureDev",
                        direction="column",
                        align_items="center",
                        class_name="text-xl font-light color-secondary",
                    ),
                    direction="column",
                    align_items="center",
                ),
                class_name="ring-1 ring-black/30 dark:ring-white/30 rounded-2xl p-4",
            ),
            class_name="pb-16 mt-24 px-2",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        direction="column",
        id="Populares",
        align_items="center",
        justify_content="center",
        margin_y="20rem",
    )


class MyApp(rx.App):
    def __init__(self, **kwargs):
        self.font_name = rx.Var("")
        super().__init__(**kwargs)

    def handleInputChange(self, event):
        self.font_name.value = event.target.value

    def handleSubmit(self, event):
        event.preventDefault()
        self.stylesheets = [
            f"https://fonts.googleapis.com/css2?family={self.font_name.value}:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
        ]

    def render(self):
        return rx.form(
            rx.input(
                type="text",
                placeholder="Nombre de la fuente por ejemplo: Sedan SC",
                value=self.font_name.value,
                on_change=self.handleInputChange,
            ),
            rx.button("Ver", type="submit"),
            direction="row",
            align_items="center",
            space_x="2",
            margin_y="8rem",
            max_width="sm",
            on_submit=self.handleSubmit,
        )


app = MyApp(style=styles.BASE_STYLE)
app.add_page(index)
app.compile()
