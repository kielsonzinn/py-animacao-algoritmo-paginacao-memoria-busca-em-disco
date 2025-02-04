import pygame
import random
import time

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Algoritmos de Busca no Disco')

WHITE = (255, 255, 255)
GRAY = (211, 211, 211)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)

disk_size = 700
num_requests = 10


def draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados=[]):
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (50, HEIGHT // 2), (WIDTH - 50, HEIGHT // 2), 5)

    for request, number in zip(requests, request_numbers):
        if number in numbers_ja_processados:
            pygame.draw.circle(screen, GREEN, (50 + request, HEIGHT // 2), 10)
        else:
            pygame.draw.circle(screen, BLUE, (50 + request, HEIGHT // 2), 10)

        font = pygame.font.SysFont(None, 16)
        text = font.render(str(number), True, WHITE)
        screen.blit(text, (50 + request - text.get_width() // 2, HEIGHT // 2 - 5))

    pygame.draw.circle(screen, RED, (50 + head_position, HEIGHT // 2), 15)

    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Algoritmo: {algorithm_name}", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

    instruction = font.render("Pressione ESPAÇO para voltar", True, BLACK)
    screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, HEIGHT - 50))

    pygame.display.update()


def fcfs_algorithm():
    requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
    request_numbers = random.sample(range(1, 11), len(requests))
    head_position = 50
    algorithm_name = 'FCFS (First Come, First Served)'

    ordered_requests = []
    for i in range(1, 11):
        pos = request_numbers.index(i)
        ordered_requests.append(requests[pos])

    numbers_ja_processados = []
    for request in ordered_requests:
        while head_position != request:
            draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
            time.sleep(0.01)
            if head_position < request:
                head_position += 1
            elif head_position > request:
                head_position -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    return True
        pos = requests.index(request)
        numbers_ja_processados.append(request_numbers[pos])
        time.sleep(0.5)

    return False


def sstf_algorithm():
    requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
    request_numbers = random.sample(range(1, 11), len(requests))
    head_position = 350
    algorithm_name = 'SSTF (Shortest Seek-Time First)'
    requests_copy = requests.copy()
    first = True
    numbers_ja_processados = []
    while requests_copy:
        closest_request = min(requests_copy, key=lambda r: abs(r - head_position))
        while head_position != closest_request:
            draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
            if first:
                time.sleep(1.00)
                first = False
            else:
                time.sleep(0.01)

            if head_position < closest_request:
                head_position += 1
            elif head_position > closest_request:
                head_position -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    return True
        pos = requests.index(closest_request)
        numbers_ja_processados.append(request_numbers[pos])
        requests_copy.remove(closest_request)
        time.sleep(0.5)

    return False


def scan_algorithm():
    head_position = 0
    direction = 1
    algorithm_name = 'SCAN (Elevador)'

    while True:
        if direction == 1:
            requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
            request_numbers = random.sample(range(1, 11), len(requests))
            numbers_ja_processados = []

            for request in requests:
                while head_position < request:
                    draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                    time.sleep(0.01)
                    head_position += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                            return True
                pos = requests.index(request)
                numbers_ja_processados.append(request_numbers[pos])
                time.sleep(0.5)

            while head_position <= 700:
                draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                time.sleep(0.01)
                head_position += 1

            direction = -1
        else:
            requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
            request_numbers = random.sample(range(1, 11), len(requests))
            numbers_ja_processados = []

            for request in reversed(requests):
                while head_position > request:
                    draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                    time.sleep(0.01)
                    head_position -= 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                            return True
                pos = requests.index(request)
                numbers_ja_processados.append(request_numbers[pos])
                time.sleep(0.5)

            while head_position >= 0:
                draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                time.sleep(0.01)
                head_position -= 1

            direction = 1


def cscan_algorithm():
    head_position = 0
    algorithm_name = 'C-SCAN (Circular SCAN)'

    while True:
        requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
        request_numbers = random.sample(range(1, 11), len(requests))
        numbers_ja_processados = []

        for request in requests:
            while head_position < request:
                draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                time.sleep(0.01)
                head_position += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                        return True
            pos = requests.index(request)
            numbers_ja_processados.append(request_numbers[pos])
            time.sleep(0.5)

        while head_position <= 700:
            draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
            time.sleep(0.01)
            head_position += 1

        head_position = 0


def look_algorithm():
    requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
    request_numbers = random.sample(range(1, 11), len(requests))
    head_position = requests[0]
    direction = 1
    algorithm_name = 'LOOK'

    while True:
        if direction == 1:
            numbers_ja_processados = []
            for request in requests:
                while head_position < request:
                    draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                    time.sleep(0.01)
                    head_position += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                            return True
                pos = requests.index(request)
                numbers_ja_processados.append(request_numbers[pos])
                time.sleep(0.5)
            direction = -1
        else:
            numbers_ja_processados = []
            for request in reversed(requests):
                while head_position > request:
                    draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                    time.sleep(0.01)
                    head_position -= 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                            return True
                pos = requests.index(request)
                numbers_ja_processados.append(request_numbers[pos])
                time.sleep(0.5)
            direction = 1


def clook_algorithm():
    algorithm_name = 'C-LOOK'

    while True:
        requests = sorted([random.randint(50, disk_size) for _ in range(num_requests)])
        request_numbers = random.sample(range(1, 11), len(requests))
        head_position = requests[0]
        numbers_ja_processados = []

        for request in requests:
            while head_position < request:
                draw_disk(head_position, requests, request_numbers, algorithm_name, numbers_ja_processados)
                time.sleep(0.01)
                head_position += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                        return True
            pos = requests.index(request)
            numbers_ja_processados.append(request_numbers[pos])
            time.sleep(0.5)


def main():
    running = True
    selected_algorithm = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_algorithm = fcfs_algorithm
                elif event.key == pygame.K_2:
                    selected_algorithm = sstf_algorithm
                elif event.key == pygame.K_3:
                    selected_algorithm = scan_algorithm
                elif event.key == pygame.K_4:
                    selected_algorithm = cscan_algorithm
                elif event.key == pygame.K_5:
                    selected_algorithm = look_algorithm
                elif event.key == pygame.K_6:
                    selected_algorithm = clook_algorithm
                elif event.key == pygame.K_SPACE:
                    selected_algorithm = None

        if selected_algorithm:
            if selected_algorithm():
                selected_algorithm = None

        else:
            screen.fill(WHITE)
            font = pygame.font.SysFont(None, 36)
            text = font.render("Escolha um algoritmo (1-6):", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))

            instructions = [
                "1 - FCFS (First Come, First Served)",  # 100%
                "2 - SSTF (Shortest Seek-Time First)",  # 100%
                "3 - SCAN (Elevador)",  # 100%
                "4 - C-SCAN (Circular SCAN)",  # 100%
                "5 - LOOK",  # 100%
                "6 - C-LOOK"  # 100%
            ]
            for i, instruction in enumerate(instructions, start=1):
                instruction_text = font.render(instruction, True, BLACK)
                screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, 100 + i * 30))

            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
