from src.logic.app import App


def main() -> None:

    app = App()
    app.refresh_offers()


if __name__ == '__main__':
    main()