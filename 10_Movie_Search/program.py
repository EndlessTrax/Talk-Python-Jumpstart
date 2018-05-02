import requests.exceptions
import movie_svc


def main():
    print_header()
    search_loop_event()


def print_header():
    print('---------------------')
    print('  Movie Search App')
    print('---------------------')
    print()


def search_loop_event():
    search = 'ONCE_THROUGH_LOOP'
    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print("Error: Search text is required")
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print('exiting...')


if __name__ == '__main__':
        main()
