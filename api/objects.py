from __future__ import annotations

from typing import Any, Iterator, Tuple

__all__ = ("User", "Guild")


class _SlotsReprMixin:
    __slots__ = ()

    def __repr__(self) -> str:
        inner = ", ".join(
            (f"{k}={v!r}" for k, v in self.get_slotted_items() if v and not k.startswith("_"))
        )
        return f"{self.__class__.__name__}({inner})"

    def get_slotted_items(self) -> Iterator[Tuple[str, Any]]:
        for slot in self.__slots__:
            yield slot, getattr(self, slot)


class User(_SlotsReprMixin):
    """
    Fetch informations about a discord user.

    Attributes
    ----------
    user_id: int
        The user's ID.
    user_name: str
        The user's Discord username.
    is_bot: bool
        Check with "is_bot" if the user is a bot.
    avatar_url: str
        Get the avatar url from the user.
    creation_date: Optional[int]
        Get the creation_date from the account.
    creation_timestamp: int
        The user's creation date as timestamp as integer.
    """

    __slots__ = (
        "user_id",
        "user_name",
        "is_bot",
        "banner_url",
        "creation_date",
        "creation_timestamp",
    )

    def __init__(
            self,
            user_id: int,
            data: dict,
    ):
        self.user_id: int = user_id
        self.user_name: str = str(data["username"])
        self.is_bot: bool = bool(data["bot"])
        self.avatar_url: str = str(data["avatar_url"])
        self.banner_url: str = str(data["banner_url"])
        self.creation_timestamp: int = int(data["creation_timestamp"])
        self.creation_date: int = int(data["creation_date"])


class Guild(_SlotsReprMixin):
    """
    Fetch informations about a discord guild.

    Attributes
    ----------
    guild_id: int
        The guild's ID.
    guild_name: str
        The user's Discord username. 
    is_bot: bool
        Check with "is_bot" if the user is a bot.
    avatar_url: str
        Get the avatar url from the user.
    creation_date: int
        Get the creation_date from the account.
    creation_timestamp: int
        The user's creation date as timestamp as integer.
    """

    __slots__ = (
        "guild_id",
        "guild_name",
        # Not released yet: "is_partnered"
        # Not released yet: "is_verified"
        # Not released yet: "description"
        "roles_count",
        "emoji_count",
        "user_count",
        # Not released yet: "online_users"
        # Not released yet: "offline_users"
        # Not releaed yet: "banner_url",
        "guildcreation_timestamp",
        "guildcreation_timestamp",
    )

    def __init__(
            self,
            guild_id: int,
            data: dict,
    ):
        self.guild_id: int = guild_id
        self.guild_name: str = str(data["guildname"])
        # Not released yet: self.is_partnered: bool = bool(data["is_partnered"])
        # Not released yet: self.is_verified: bool = bool(data["is_verified"])
        # Not released yet: self.description: str = str(data["description"])
        self.owner_id: int = int(data["guildownerID"])
        self.icon_url: bool = bool(data["guildicon_url"])
        self.roles_count: int = int(data["guildroles_count"])
        self.user_count: int = int(data["guildusers_count"])
        self.emoji_count: int = int(data["guildemojis_count"])
        # Not released yet: self.online_users: str = str(data["online_users"])
        # Not released yet: self.offline_users: str = str(data["offline_users"])
        # Not released yet: self.banner_url: str = str(data["banner_url"])
        self.guildcreation_timestamp: int = int(data["guildcreation_timestamp"])
        self.guildcreation_date: int = int(data["guildcreation_date"])
