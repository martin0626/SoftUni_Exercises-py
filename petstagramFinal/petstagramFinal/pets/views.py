from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from petstagramFinal.pets.forms import PetForm, CommentsForm, EditForm
from petstagramFinal.pets.models import Pet, Like, Comment


def pets(request):
    pet = Pet.objects.all()

    context = {
        'Pets': pet
    }
    return render(request, 'pets/pet_list.html', context)


def pets_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    comments = Comment.objects.filter(pet_id=pk)
    owner = User.objects.get(pk=pet.user_id)
    is_liked = Like.objects.filter(
        user_id=request.user.id,
        pet_id=pet.id,
    )
    print(list(is_liked))

    context = {
        'Pet': pet,
        'form': CommentsForm(),
        "comments": comments,
        "owner": owner,
        'is_liked': is_liked,
    }
    return render(request, 'pets/pet_detail.html', context)


def make_comment(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentsForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
            user_id=request.user.id
        )
        comment.save()

    return redirect('pet details', pk)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    is_liked = Like.objects.filter(
        user_id=request.user.id,
        pet_id=pet.id,
    )

    if is_liked:
        list(is_liked)[0].delete()
    else:
        like = Like(pet_id=pet.id, user_id=request.user.id)
        like.save()

    return redirect('pet details', pet.id)


def create_pet(request):

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user_id = request.user.id
            pet.save()
            return redirect('pets list')

    context = {
        'form': PetForm()
    }

    return render(request, 'pets/pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets list')
    context = {
        'form': EditForm(
            initial=pet.__dict__
        ),
    }

    return render(request, 'pets/pet_edit.html', context)


def del_photo(request, pk):

    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        pet.delete()
        return redirect('pets list')

    return render(request, 'pets/pet_delete.html')
