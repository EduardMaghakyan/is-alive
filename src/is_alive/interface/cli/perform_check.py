from is_alive.dependency_container import Application

if __name__ == "__main__":
    app = Application()
    app.check_availability(url="https://example.com/")
