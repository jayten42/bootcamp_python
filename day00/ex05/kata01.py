if __name__ == '__main__':
    language = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf'
    }
    fmt = '{} was created by {}'
    print('\n'.join(fmt.format(key, value) for key, value in language.items()))
