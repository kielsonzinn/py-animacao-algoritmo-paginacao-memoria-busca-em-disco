import pygame
import time
import collections

WIDTH, HEIGHT = 550, 400
BACKGROUND_COLOR = (30, 30, 30)
FRAME_COLOR = (200, 200, 200)
PAGE_COLOR = (50, 150, 250)
REPLACE_COLOR = (250, 50, 50)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 24

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algoritmos de Substituição de Página")
font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()


def draw_memory(frames, highlight=None, next_page=None, message="Pressione espaço para a próxima página"):
    screen.fill(BACKGROUND_COLOR)
    for i, page in enumerate(frames):
        color = REPLACE_COLOR if highlight == i else PAGE_COLOR
        pygame.draw.rect(screen, color, (100 + i * 120, 150, 100, 100))
        text = font.render(str(page), True, TEXT_COLOR)
        screen.blit(text, (130 + i * 120, 190))

    message_text = font.render(message, True, TEXT_COLOR)
    screen.blit(message_text, (WIDTH // 2 - 150, 50))

    if next_page is not None:
        next_page_text = font.render(f"Próxima página: {next_page}", True, TEXT_COLOR)
        screen.blit(next_page_text, (WIDTH // 2 - 150, 90))

    pygame.display.flip()


def fifo_simulation(pages, frame_count):
    queue = collections.deque()
    frames = []
    page_index = 0
    while page_index < len(pages):
        page = pages[page_index]
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                removed = queue.popleft()  # Primeiro a entrar, primeiro a sair
                frames[frames.index(removed)] = page
            queue.append(page)

        next_page = pages[page_index + 1] if page_index + 1 < len(pages) else None
        draw_memory(frames, highlight=frames.index(page), next_page=next_page)
        page_index += wait_for_space()


def lru_simulation(pages, frame_count):
    frames = []
    access_time = {}
    page_index = 0
    while page_index < len(pages):
        page = pages[page_index]
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                lru_page = min(frames, key=lambda x: access_time[x])  # O que foi acessado há mais tempo, ou seja, o tempo mais antigo de acesso
                frames[frames.index(lru_page)] = page

        access_time[page] = time.time()
        next_page = pages[page_index + 1] if page_index + 1 < len(pages) else None
        draw_memory(frames, highlight=frames.index(page), next_page=next_page)
        page_index += wait_for_space()


def wait_for_space():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 1


def main():
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frame_count = 3
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)
        text = font.render("Pressione F para FIFO ou L para LRU", True, TEXT_COLOR)
        screen.blit(text, (135, 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fifo_simulation(pages, frame_count)
                elif event.key == pygame.K_l:
                    lru_simulation(pages, frame_count)

    pygame.quit()


if __name__ == "__main__":
    main()
