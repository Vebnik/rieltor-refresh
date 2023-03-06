from src.schedule.tasks import refresh_offer
from src.logic.app import App


def main() -> None:
    app = App()
    refresh_offer(app)


if __name__ == '__main__':
    main()