import B_mp4_video_single

total_loops = 20
seed_number = 634
static_seed_for_interpolation = 643
smoothness = 2.0


i = 0
while i < total_loops:
    mp4_video.main(seed_number, static_seed_for_interpolation, smoothness)
    seed_number = seed_number + 100
    static_seed_for_interpolation = static_seed_for_interpolation + 100
    i += 1
    
    
