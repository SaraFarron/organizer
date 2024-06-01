from __future__ import annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent

SIGNUP_BUTTON = c.Button(text="SignUp", on_click=GoToEvent(url="/signup"))
PROFILE_BUTTON = c.Button(text="Profile", on_click=GoToEvent(url="/profile"))


def home_page() -> list[AnyComponent]:
    """Home page of the app."""
    return [...]


def get_navbar() -> c.Navbar:
    """Get navbar."""
    return c.Navbar(...)


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
        c.Footer(...),
    ]
