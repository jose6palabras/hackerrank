import re
import logging

logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    level  = logging.INFO, # events level in logger
)

class ArticleManager:
    def __init__(self, article_text, options=None):
        if options is None:
            options = {}
        
        self.article_text = article_text
        self.pages = []
        self.words = []
        self.totalpages_doc = 0
        logging.info('setting some values')
        self.options = {
            'words_per_line': options['words_per_line'] or 12 if 'words_per_line' in options else 12,
            'lines_per_page': options['lines_per_page'] or 20 if 'lines_per_page' in options else 20,
            'payment_structure': options.get('payment_structure', {
                1: 30,
                2: 30,
                3: 60,
                4: 100,
                'default': 0,
            })
        }

    def split_into_pages(self):
        words_per_line = self.options['words_per_line']
        lines_per_page = self.options['lines_per_page']
        logging.info('main step, calculating number of pages')
        self.words = re.split(' ', self.article_text.strip())
        total_pages = (len(self.words) // (words_per_line * lines_per_page))  # equivalent to math.ceil
        self.totalpages_doc = total_pages

        for i in range(total_pages + 1):
            page_words = self.words[i * words_per_line * lines_per_page:(i + 1) * words_per_line * lines_per_page]
            page_lines = []

            # Split the page into lines
            for j in range(0, len(page_words), words_per_line):
                page_lines.append(' '.join(page_words[j:j + words_per_line]))

            # Join the lines into a single string
            page = '\n'.join(page_lines)

            # Add the page to the list of pages
            self.pages.append(page)

    def calculate_payment(self):
        payment_structure = self.options['payment_structure']
        total_pages = self.totalpages_doc

        # Find the payment for the total number of pages
        payment = payment_structure.get(total_pages, payment_structure['default'])

        return payment

    def display_pages(self):
        payment = self.calculate_payment()
        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")

        print(f"Total Pages: {self.totalpages_doc}")
        print(f"Payment Due: ${payment}")

    def process_article(self):
        self.split_into_pages()
        self.display_pages()

# Example usage
logging.info('call the class')
article_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
laborum
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
laborum
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
laborum
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla."""

if type(article_text)==str:
  article_manager = ArticleManager(article_text)
  article_manager.process_article()
else: print("non-string input")