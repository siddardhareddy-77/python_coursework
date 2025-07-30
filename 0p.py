from collections import Counter, defaultdict

def get_user_and_text(msg):
    parts = msg.split(':', 1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return None, None

def get_confirmed_user(messages, prompt="Input user: "):
    users = sorted({get_user_and_text(msg)[0] for msg in messages if get_user_and_text(msg)[0]})
    if not users:
        print("No users found in chat.")
        return None
    print(f"Available users: {', '.join(users)}")
    user = input(prompt).strip()
    if user in users:
        return user
    else:
        print(f"User '{user}' not found.")
        return None

def count_total_messages(messages):
    print(f"Total messages: {len(messages)}")

def identify_unique_users(messages):
    users = {get_user_and_text(msg)[0] for msg in messages if get_user_and_text(msg)[0]}
    print(f"Unique users in the chat: {users}")

def count_total_words(messages):
    total_words = sum(len(get_user_and_text(msg)[1].split()) for msg in messages if get_user_and_text(msg)[1])
    print(f"Total words in the chat: {total_words}")

def average_words_per_message(messages):
    word_counts = [len(get_user_and_text(msg)[1].split()) for msg in messages if get_user_and_text(msg)[1]]
    avg = sum(word_counts) / len(messages) if messages else 0
    print(f"Average words per message: {round(avg, 2)}")

def find_longest_message(messages):
    if not messages:
        print("No messages available.")
        return
    longest_msg = max(messages, key=lambda m: len(get_user_and_text(m)[1]) if get_user_and_text(m)[1] else 0)
    print(f'Longest message: "{longest_msg}"')

def most_active_user(messages):
    count = Counter(get_user_and_text(msg)[0] for msg in messages if get_user_and_text(msg)[0])
    if not count:
        print("No users found.")
        return
    user, cnt = count.most_common(1)[0]
    print(f"Most active user: {user} ({cnt} messages)")

def message_count_for_user(messages):
    user = get_confirmed_user(messages)
    if not user:
        return
    cnt = sum(1 for msg in messages if get_user_and_text(msg)[0] == user)
    print(f"Messages sent by {user}: {cnt}")

def most_frequent_word_by_user(messages):
    user = get_confirmed_user(messages)
    if not user:
        return
    words = []
    for msg in messages:
        u, text = get_user_and_text(msg)
        if u == user:
            words.extend(text.lower().split())
    if not words:
        print(f"No messages found for user {user}.")
        return
    most_common_word, _ = Counter(words).most_common(1)[0]
    print(f'Most frequent word used by {user}: "{most_common_word}"')

def first_and_last_message_by_user(messages):
    user = get_confirmed_user(messages)
    if not user:
        return
    user_msgs = [msg for msg in messages if get_user_and_text(msg)[0] == user]
    if not user_msgs:
        print(f"No messages found for user {user}.")
        return
    print(f'First message by {user}: "{user_msgs[0]}"')
    print(f'Last message by {user}: "{user_msgs[-1]}"')

def check_user_present(messages):
    user = input("Input user: ").strip()
    users = {get_user_and_text(msg)[0] for msg in messages if get_user_and_text(msg)[0]}
    if user in users:
        print(f"User '{user}' found in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")

def common_repeated_words(messages):
    all_words = []
    for msg in messages:
        text = get_user_and_text(msg)[1]
        if text:
            all_words.extend(text.lower().split())
    freq = Counter(all_words)
    common_words = {word for word, count in freq.items() if count > 1}
    print(f"Common repeated words: {common_words}")

def user_with_longest_average_message(messages):
    user_word_counts = defaultdict(list)
    for msg in messages:
        user, text = get_user_and_text(msg)
        if user:
            word_count = len(text.split()) if text else 0
            user_word_counts[user].append(word_count)
    if not user_word_counts:
        print("No messages to analyze.")
        return
    avg_lengths = {user: sum(words)/len(words) for user, words in user_word_counts.items()}
    user, avg = max(avg_lengths.items(), key=lambda x: x[1])
    print(f"User with longest average message: {user} (avg {round(avg, 2)} words)")

def messages_mentioning_user(messages):
    user = input("Input user: ").strip().lower()
    count = 0
    for msg in messages:
        text = get_user_and_text(msg)[1]
        if text and user in text.lower():
            count += 1
    print(f"Messages mentioning '{user}': {count}")

def remove_duplicate_messages(messages):
    unique_msgs = list(dict.fromkeys(messages))
    print(f"Unique messages count: {len(unique_msgs)}")

def sort_messages_alphabetically(messages):
    for msg in sorted(messages):
        print(msg)

def extract_questions(messages):
    questions = [msg for msg in messages if get_user_and_text(msg)[1] and '?' in get_user_and_text(msg)[1]]
    if questions:
        for q in questions:
            print(q)
    else:
        print("No questions found in the chat.")

def calculate_reply_ratio(messages):
    pair = input("Input two users (format: user1 and user2): ").strip()
    if " and " not in pair:
        print("Input format incorrect.")
        return
    user1, user2 = [u.strip() for u in pair.split(" and ", 1)]
    replies = sum(
        1 for i in range(len(messages) - 1)
        if get_user_and_text(messages[i])[0] == user1 and get_user_and_text(messages[i+1])[0] == user2
    )
    print(f"Reply ratio from {user2} to {user1}: {replies} replies")

def check_for_deleted_messages(messages):
    deleted_text = "This message was deleted"
    count = sum(
        1 for m in messages
        if get_user_and_text(m)[1] == deleted_text
    )
    print(f"Deleted messages found: {count}")

def print_menu():
    print(
        "\nChoose an analysis option:"
        "\n1. Count total number of messages"
        "\n2. Identify unique users in the chat"
        "\n3. Count total words in the chat"
        "\n4. Calculate average words per message"
        "\n5. Find the longest message sent"
        "\n6. Find the most active user"
        "\n7. Get message count for a specific user"
        "\n8. Find the most frequently used word by a specific user"
        "\n9. Retrieve the first and last message sent by a user"
        "\n10. Check if a user is present in the chat"
        "\n11. Find commonly repeated words"
        "\n13. Identify the user with the longest average message length"
        "\n14. Count how many messages mention a specific user"
        "\n15. Remove duplicate messages"
        "\n16. Sort messages alphabetically"
        "\n17. Extract all questions asked in the chat"
        "\n18. Calculate the reply ratio between two users"
        "\n19. Check for deleted messages"
        "\n0. Exit"
    )

def main():
    try:
        n = int(input("Enter the number of messages: "))
    except ValueError:
        print("Invalid number.")
        return
    messages = []
    print("Enter messages one by one (format: Name: message)")
    for _ in range(n):
        messages.append(input())

    menu_actions = {
        '1': count_total_messages,
        '2': identify_unique_users,
        '3': count_total_words,
        '4': average_words_per_message,
        '5': find_longest_message,
        '6': most_active_user,
        '7': message_count_for_user,
        '8': most_frequent_word_by_user,
        '9': first_and_last_message_by_user,
        '10': check_user_present,
        '11': common_repeated_words,
        '13': user_with_longest_average_message,
        '14': messages_mentioning_user,
        '15': remove_duplicate_messages,
        '16': sort_messages_alphabetically,
        '17': extract_questions,
        '18': calculate_reply_ratio,
        '19': check_for_deleted_messages,
    }

    while True:
        print_menu()
        choice = input("Enter your choice (0 to exit): ").strip()
        if choice == '0':
            print("Exiting...")
            break
        action = menu_actions.get(choice)
        if action:
            action(messages)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
