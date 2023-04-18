import pygame


class Menu:
    def __init__(self, screen):
        self.menu_open = False
        self.width, self.height = screen
        self.font = pygame.font.Font(None, 30)
        self.button_width = 100
        self.button_height = 40
        self.button_margin = 20

        self.screen = pygame.display.get_surface()

    def toggle_menu(self):
        self.menu_open = not self.menu_open
        return self.menu_open

    def get_buttons(self):
        return [
            (
                "Replay",
                self.button_width,
                self.button_height,
                self.width / 3 - self.button_width / 3,
                self.height / 3 - self.button_height / 3 - self.button_margin
            ),
            (
                "Mute",
                self.button_width,
                self.button_height,
                self.width / 3 - self.button_width / 3,
                self.height / 3 + self.button_margin
            ),
            (
                "Unmute",
                self.button_width,
                self.button_height,
                self.width / 3 - self.button_width / 3,
                self.height / 3 + 2.2 * self.button_height / 3 + 2.2 * self.button_margin
            ),
            (
                "Quit",
                self.button_width,
                self.button_height,
                self.width / 3 - self.button_width / 3,
                self.height / 3 + 3.8 * self.button_height / 3 + 3.8 * self.button_margin
            ),
        ]

    def show(self):
        buttons = self.get_buttons()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.menu_open = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (text, w, h, x, y) in enumerate(buttons):
                        if x <= event.pos[0] <= x + w and y <= event.pos[1] <= y + h:
                            if i == 0:
                                return "replay"
                            elif i == 1:
                                return "mute"
                            elif i == 2:
                                return "unmute"
                            elif i == 3:
                                return "quit"

                if not self.menu_open:
                    return

            self.screen.fill((200, 200, 200))

            for text, w, h, x, y in buttons:
                button_rect = pygame.Rect(x, y, w, h)
                pygame.draw.rect(self.screen, (150, 150, 150), button_rect)
                button_text = self.font.render(text, True, (255, 255, 255))
                self.screen.blit(
                    button_text,
                    (x + w / 2 - button_text.get_width() / 2, y + h / 2 - button_text.get_height() / 2)
                )

            pygame.display.flip()
