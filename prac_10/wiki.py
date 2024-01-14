
import wikipedia

def search_wikipedia():
    while True:
        query = input("Enter a Wikipedia search term or page title (or just hit enter to quit): ")
        if query == "":
            break

        try:
            # Getting the summary of the page
            summary = wikipedia.summary(query)
            page = wikipedia.page(query)
            print(f"Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary: {summary}
")

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_wikipedia()
