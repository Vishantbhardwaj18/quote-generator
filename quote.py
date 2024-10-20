import random

# Expanded list of quotes
quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "The mind is everything. What you think you become. - Buddha",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The best way to predict the future is to create it. - Peter Drucker",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston S. Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "You cannot shake hands with a clenched fist. - Indira Gandhi",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Don't count the days; make the days count. - Muhammad Ali",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Life is short, and it's up to you to make it sweet. - Sarah Louise Delany",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "The best revenge is massive success. - Frank Sinatra",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "You can't use up creativity. The more you use, the more you have. - Maya Angelou",
    "Dream big and dare to fail. - Norman Vaughan",
    "If you can dream it, you can achieve it. - Zig Ziglar",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful. - Joshua J. Marine",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "If you're going through hell, keep going. - Winston S. Churchill",
    "The harder you work for something, the greater you'll feel when you achieve it. - Anonymous",
    "Dream it. Wish it. Do it. - Anonymous",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "It is never too late to be what you might have been. - George Eliot",
    "Your limitation—it's only your imagination. - Anonymous",
    "Push yourself, because no one else is going to do it for you. - Anonymous",
    "Great things never come from comfort zones. - Anonymous",
    "Dream bigger. Do bigger. - Anonymous",
    "Success doesn’t just find you. You have to go out and get it. - Anonymous",
    "The harder you work for something, the greater you’ll feel when you achieve it. - Anonymous",
    "Dream it. Wish it. Do it. - Anonymous",
    "Don’t stop when you’re tired. Stop when you’re done. - Anonymous",
    "Wake up with determination. Go to bed with satisfaction. - Anonymous",
    "Do something today that your future self will thank you for. - Anonymous",
    "Little things make big days. - Anonymous",
    "It’s going to be hard, but hard does not mean impossible. - Anonymous",
    "Don’t wait for opportunity. Create it. - Anonymous",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths. - Anonymous",
    "The key to success is to focus on goals, not obstacles. - Anonymous",
    "Dream bigger. Do bigger. - Anonymous",
    "Believe in yourself and all that you are. - Christian D. Larson",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Everything you can imagine is real. - Pablo Picasso",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "The future depends on what you do today. - Mahatma Gandhi",
    "The secret of getting ahead is getting started. - Mark Twain",
    "Keep your eyes on the stars, and your feet on the ground. - Theodore Roosevelt",
    "What we think, we become. - Buddha",
    "It’s not whether you get knocked down; it’s whether you get up. - Vince Lombardi",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "I am not a product of my circumstances. I am a product of my decisions. - Stephen R. Covey",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "What we fear doing most is usually what we most need to do. - Tim Ferriss",
    "If you don’t like something, change it. If you can’t change it, change your attitude. - Maya Angelou",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "If you want to achieve greatness stop asking for permission. - Anonymous",
    "I never dreamed about success. I worked for it. - Estée Lauder"
]

def get_random_quote():
    """Returns a random quote from the quotes list."""
    return random.choice(quotes)

def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        input("Press Enter to get a random quote or type 'exit' to quit: ")
        print("\n" + get_random_quote() + "\n")
        # Check if the user wants to exit
        if input("Type 'exit' to quit or press Enter to see another quote: ").strip().lower() == 'exit':
            break
    print("Thank you for using the Random Quote Generator!")

if __name__ == "__main__":
    main()
