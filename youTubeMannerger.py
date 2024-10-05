import json

# Load existing videos from the file, or initialize an empty list
def loadVedios():
    try:
        with open('json.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save videos to the file
def saveVedios(vedios):
    with open('json.txt', 'w') as file:
        json.dump(vedios, file, indent=4)

# Add a new video
def addVedio(vedios):
    vedio = input('Enter video name: ')
    time = input('Enter video time: ')
    vedios.append({'vedio name': vedio, 'vedio time': time})
    saveVedios(vedios)
    print(f'Video "{vedio}" added successfully!\n')

# Get (display) all videos
def getVediov(vedios):
    if not vedios:
        print("No videos available.")
        return
    
    for index, items in enumerate(vedios):
        print(f"{str(index + 1)}) Video name = {items['vedio name']}, Time = {items['vedio time']}")

# Update an existing video
def updateVedio(vedios):
    if vedios:
        try:
            getVediov(vedios)
            index = int(input('Enter the video number to update: ')) - 1
            if 0 <= index < len(vedios):
                vedios[index]['vedio name'] = input('Enter new video name: ')
                vedios[index]['vedio time'] = input('Enter new video time: ')
                saveVedios(vedios)  # Save the updated list to the file
                print('Video updated successfully!\n')
            else:
                print('Invalid video number.\n')
        except ValueError:
            print('Please enter a valid number.\n')

# Delete a video
def deleteVedio(vedios):
    if vedios:
        try:
            getVediov(vedios)  # Display the list of videos
            index = int(input('Enter the number of the video to delete: ')) - 1
            
            if 0 <= index < len(vedios):  # Check if the index is valid
                deleted = vedios.pop(index)  # Delete the video by index
                saveVedios(vedios)  # Save the updated list to the file
                print(f'Video "{deleted["vedio name"]}" deleted successfully!\n')
            else:
                print('Invalid video number.\n')
        except ValueError:
            print('Please enter a valid number.\n')
    else:
        print('No videos to delete.\n')

# Main program loop
while True:
    print('1) Add New Video')
    print('2) Update Video')
    print('3) Get Video List')
    print('4) Delete Video')
    print('5) Exit')
    
    try:
        choice = int(input('Enter your choice (1, 2, 3, 4, 5): '))
        vedios = loadVedios()

        match choice:
            case 1:
                addVedio(vedios)
            case 2:
                updateVedio(vedios)
            case 3:
                getVediov(vedios)
            case 4:
                deleteVedio(vedios)
            case 5:
                print('Exiting program.')
                break
            case _:
                print('Please enter a valid choice.\n')
    except ValueError:
        print('Invalid input. Please enter a number.\n')
