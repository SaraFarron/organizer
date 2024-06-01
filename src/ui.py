from __future__ import annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent

SIGNUP_BUTTON = c.Button(text="SignUp", on_click=GoToEvent(url="/signup"))
PROFILE_BUTTON = c.Button(text="Profile", on_click=GoToEvent(url="/profile"))


def home_page() -> list[AnyComponent]:
    """Home page of the app."""
    return []


def get_navbar() -> c.Navbar:
    """Get navbar."""
    return c.Navbar(
        start_links=[
            c.Link(
                components=[c.Text(text="Home")],
                on_click=GoToEvent(url="/"),
            ),
            c.Link(
                components=[c.Text(text="Income")],
                on_click=GoToEvent(url="/charts/income"),
            ),
            c.Link(
                components=[c.Text(text="Expences")],
                on_click=GoToEvent(url="/charts/expences"),
            ),
            c.Link(
                components=[c.Text(text="Profits")],
                on_click=GoToEvent(url="/charts/profits"),
            ),
        ],
    )


def page_wrapper(components: list[AnyComponent], title: str | None = None) -> list[AnyComponent]:
    """
    Base page for the app.

    Includes title, navbar and footer.
    """
    return [
        c.PageTitle(text=f"App - {title}" if title else "Title"),
        get_navbar(),
        c.Page(
            components=components,
        ),
        c.Footer(
            extra_text="Made with ❤️ by SaraFarron",
            links=[
                c.Link(
                    components=[c.Text(text="GitHub")],
                    on_click=GoToEvent(url="https://github.com/SaraFarron/organizer"),
                ),
            ],
        ),
    ]
