import A_mp4_circular_interpolations_single

total_loops = 5
#seed_number = 634
#static_seed_for_interpolation = 643
#smoothness = 2.0

truncationX = 0.1

i = 1
while i < total_loops:
    videoname = 'results/circular_truncation_%s.mp4' % i
    mp4_circular_interpolations.main(videoname, truncationX)
    #seed_number = seed_number + 100
    #static_seed_for_interpolation = static_seed_for_interpolation + 100
    truncationX = truncationX + 0.1
    i += 1
    
    
    
    
    
