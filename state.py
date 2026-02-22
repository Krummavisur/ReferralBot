class MessageState:
    def __init__(self) -> None:
        self._last_bot_messages: dict[int, int] = {}
        self._anchor_messages: dict[int, int] = {}
        self._users: set[int] = set()

    def add_user(self, chat_id: int) -> None:
        self._users.add(chat_id)

    def get_users(self) -> set[int]:
        return self._users
        
    def get_last_message(self, chat_id: int) -> int | None:
        return self._last_bot_messages.get(chat_id)

    def save_message(self, chat_id: int, message_id: int) -> None:
        self._last_bot_messages[chat_id] = message_id

    def has_anchor(self, chat_id: int) -> bool:
        return chat_id in self._anchor_messages

    def save_anchor(self, chat_id: int, message_id: int) -> None:
        self._anchor_messages[chat_id] = message_id
