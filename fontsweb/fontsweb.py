from rxconfig import config
import reflex as rx

import fontsweb.styles.styles as styles


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        rx.text("by uprizingFaze", class_name="text-xl text-neutral-700 ml-4"),
        rx.box(
            rx.text("FONTS", class_name="text-9xl text-neutral-700 text-center font-bold"),
            rx.text("DESINGS", class_name="text-9xl text-neutral-700 text-center font-bold"),
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
                rx.text("Free for commercial use.", class_name="py-6 text-2xl text-neutral-700"),
                class_name="ring-1 ring-neutral-300 rounded-3xl p-4",
            ),
            direction="grid",
            grid_template_columns="repeat(3, 1fr)",
            gap="2",
            padding="2",
        ),
        rx.box(
            rx.box(
                rx.text("Sitio web", class_name="text-7xl"),
                direction="column",
                align_items="center",
                padding_y="24",
            ),
            rx.box(
                rx.box(
                    rx.text("by uprizingFaze", class_name="py-12"),
                    rx.box(
                        rx.text("Inicia tus web apps", class_name="text-5xl"),
                        rx.text("usando Reflex", class_name="text-5xl"),
                        rx.text(
                            "Crea Aplicaciones web mas rápido. Crea toda tu aplicación en un solo idioma. No se preocupe por escribir API para conectar su frontend y backend.",
                            class_name="mt-8 text-neutral-700",
                        ),
                        rx.box(
                            rx.button("Comenzar ahora", class_name="mr-4", size="sm"),
                            rx.button("Github", class_name="ml-4", size="sm", variant="secondary"),
                            direction="row",
                            margin_y="12",
                        ),
                        rx.image("/cap.png", alt="hero", width=600, height=600, class_name="rounded-3xl mt-6"),
                        direction="column",
                        align_items="center",
                        margin_top="6",
                    ),
                    direction="column",
                    align_items="center",
                    class_name="ring-1 ring-neutral-300 rounded-3xl p-4 bg-gradient-to-bl from-white to-neutral-200",
                ),
            ),
        ),
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
                rx.text("Jacquard 24", class_name="text-7xl ml-8 font-semibold"),
                rx.box(
                    rx.text("Font: Jacquard 24"),
                    rx.text("Style: SemiBolt"),
                    direction="column",
                    class_name="text-xs mr-8",
                ),
                direction="row",
                justify_content="between",
            ),
            class_name="jacquard_24.className",
        ),
        rx.hr(class_name="my-4 mx-5 border-black dark:border-white"),
        direction="column",
        id="Populares",
        align_items="center",
        justify_content="center",
        margin_y="20rem",
    )


app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
app.compile()