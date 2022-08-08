import pygame

settings = {'window_size': (400, 600),
            'FPS': 30,
            'font': 'century',
            'font_size': 50,
            'caption_name': 'Gobblet Gobblers',

            'YELLOW': (255, 212, 0),
            'WHITE': (255, 255, 255),
            'BLACK': (0, 0, 0),
            'BOLD': 5,

            'reset_sleep_time': 5}


def main():
    pygame.init()
    screen = pygame.display.set_mode(settings['window_size'])
    font = pygame.font.SysFont(settings['font'], settings['font_size'])
    FPSCLOCK = pygame.time.Clock()
    FPS = settings['FPS']
    pygame.display.set_caption(settings['caption_name'])

    # p1 = Human_player(FPSCLOCK, FPS, renderer)
    # p2 = Human_player(FPSCLOCK, FPS, renderer)

    # p1 = Random_player()
    # p2 = Random_player()

    # p1 = Monte_Carlo_player()
    # p2 = Monte_Carlo_player()

    # 스코어 보드
    p1_score = 0
    p2_score = 0
    draw_score = 0

    i = 0
    while True:
        reward, done = env.move(p1, p2, (-1) ** i)  # 1,-1,1,-1...
        renderer.rendering(env)
        i += 1
        if done:
            if reward == 1:
                print("winner is p1({})".format(p1.name))
                p1_score += 1
            elif reward == -1:
                print("winner is p2({})".format(p2.name))
                p2_score += 1
            else:
                print("draw")
                draw_score += 1

            print(
                "p1({}) = {} p2({}) = {} draw = {}".format(p1.name, p1_score, p2.name, p2_score, draw_score))

            env.reset_game()
            renderer.new_game_window(env)
            i = 0


if __name__ == '__main__':
    main()
