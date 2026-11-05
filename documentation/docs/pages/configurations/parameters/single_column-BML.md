---
search:
  exclude: true
---

# single_column-BML: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [single_column-BML](../mom6examples/single_column-BML.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = False                   !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">USE_RK2 = False                 !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use RK2 instead of RK3 in the unsplit time stepping.</span>
<span id="L8">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L9">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L10">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L11">ENABLE_THERMODYNAMICS = True    !   [Boolean] default = True</span>
<span id="L12">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L13">USE_EOS = True                  !   [Boolean] default = True</span>
<span id="L14">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L15">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L16">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L17">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L18">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L19">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
<span id="L20">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L21">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L22">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L23">                                ! T&amp;S diagnostics.</span>
<span id="L24">ADIABATIC = False               !   [Boolean] default = False</span>
<span id="L25">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L26">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L27">                                ! eliminating subroutine calls.</span>
<span id="L28">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L29">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L30">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L31">                                ! development</span>
<span id="L32">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L33">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L34">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L35">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L36">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L37">USE_REGRIDDING = False          !   [Boolean] default = False</span>
<span id="L38">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L39">                                ! layered isopycnal algorithm.</span>
<span id="L40">BULKMIXEDLAYER = True           !   [Boolean] default = True</span>
<span id="L41">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L42">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L43">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L44">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L45">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L46">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L47">                                ! edges of the grid cells.</span>
<span id="L48">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L49">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L50">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L51">                                ! points.</span>
<span id="L52">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L53">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L54">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L55">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L56">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L57">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L58">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L59">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L60">DT = 3600.0                     !   [s]</span>
<span id="L61">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L62">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L63">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L64">DT_THERM = 3600.0               !   [s] default = 3600.0</span>
<span id="L65">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L66">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L67">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L68">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L69">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L70">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L71">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L72">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L73">                                ! equal to DT_THERM.</span>
<span id="L74">DT_TRACER_ADVECT = 3600.0       !   [s] default = 3600.0</span>
<span id="L75">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L76">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L77">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L78">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L79">                                ! DT_THERM.</span>
<span id="L80">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L81">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L82">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L83">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L84">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L85">THICKNESSDIFFUSE = False        !   [Boolean] default = False</span>
<span id="L86">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L87">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L88">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L89">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L90">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L91">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L92">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L93">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L94">                                ! computed.</span>
<span id="L95">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L96">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L97">                                ! step, using the specified value at the end of the step.</span>
<span id="L98">FRAZIL = True                   !   [Boolean] default = False</span>
<span id="L99">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L100">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L101">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L102">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L103">                                ! If true, apply geothermal heating.</span>
<span id="L104">BOUND_SALINITY = False          !   [Boolean] default = False</span>
<span id="L105">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L106">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L107">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L108">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L109">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L110">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L111">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L112">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L113">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L114">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L115">                                ! definition of conservative temperature.</span>
<span id="L116">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L117">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L118">                                ! state calculations.</span>
<span id="L119">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L120">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L121">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L122">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L123">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L124">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L125">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L126">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L127">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L128">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L129">NKML = 2                        !   [nondim] default = 2</span>
<span id="L130">                                ! The number of sublayers within the mixed layer if BULKMIXEDLAYER is true.</span>
<span id="L131">NKBL = 2                        !   [nondim] default = 2</span>
<span id="L132">                                ! The number of layers that are used as variable density buffer layers if</span>
<span id="L133">                                ! BULKMIXEDLAYER is true.</span>
<span id="L134">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L135">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L136">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L137">                                ! and odd numbers used for y-first.</span>
<span id="L138">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L139">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L140">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L141">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L142">                                ! first direction can not be found in the restart file.</span>
<span id="L143">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L144">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L145">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L146">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L147">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L148">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L149">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L150">                                ! updated and more robust forms of the same expressions.</span>
<span id="L151">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L152">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L153">IC_OUTPUT_FILE = &quot;MOM_IC&quot;       ! default = &quot;MOM_IC&quot;</span>
<span id="L154">                                ! The file into which to write the initial conditions.</span>
<span id="L155">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L156">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L157">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L158">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L159">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L160">                                ! The file into which to write the ocean geometry.</span>
<span id="L161">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L162">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L163">                                ! analysis and machine-learning inference.</span>
<span id="L164">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L165">                                ! If true, enables the ice shelf model.</span>
<span id="L166">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L167">                                ! If true, use the particles package.</span>
<span id="L168">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L169">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L170">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L171">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L172">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L173">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L174">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L175">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L176">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L177"></span>
<span id="L178">! === module MOM_domains ===</span>
<span id="L179">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L180">                                ! If true, the domain is zonally reentrant.</span>
<span id="L181">REENTRANT_Y = True              !   [Boolean] default = False</span>
<span id="L182">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L183">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L184">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L185">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L186">NIGLOBAL = 2                    !</span>
<span id="L187">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L188">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L189">NJGLOBAL = 2                    !</span>
<span id="L190">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L191">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L192">NIHALO = 2                      ! default = 4</span>
<span id="L193">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L194">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L195">NJHALO = 2                      ! default = 4</span>
<span id="L196">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L197">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L198"></span>
<span id="L199">! === module MOM_hor_index ===</span>
<span id="L200">! Sets the horizontal array index types.</span>
<span id="L201"></span>
<span id="L202">! === module MOM_grid ===</span>
<span id="L203">! Parameters providing information about the lateral grid.</span>
<span id="L204">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L205">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L206"></span>
<span id="L207">! === module MOM_fixed_initialization ===</span>
<span id="L208">INPUTDIR = &quot;INPUT/BATS&quot;         ! default = &quot;.&quot;</span>
<span id="L209">                                ! The directory in which input files are found.</span>
<span id="L210"></span>
<span id="L211">! === module MOM_grid_init ===</span>
<span id="L212">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L213">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L214">                                ! grid.  Current options are:</span>
<span id="L215">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L216">                                !              file set by GRID_FILE.</span>
<span id="L217">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L218">                                !     spherical - use a simple spherical grid.</span>
<span id="L219">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L220">AXIS_UNITS = &quot;degrees&quot;          ! default = &quot;degrees&quot;</span>
<span id="L221">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L222">                                !     degrees - degrees of latitude and longitude</span>
<span id="L223">                                !     m or meter(s) - meters</span>
<span id="L224">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L225">SOUTHLAT = 30.0                 !   [degrees]</span>
<span id="L226">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L227">                                ! y-axis.</span>
<span id="L228">LENLAT = 1.0                    !   [degrees]</span>
<span id="L229">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L230">WESTLON = 0.0                   !   [degrees] default = 0.0</span>
<span id="L231">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L232">                                ! x-axis.</span>
<span id="L233">LENLON = 1.0                    !   [degrees]</span>
<span id="L234">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L235">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L236">                                ! The radius of the Earth.</span>
<span id="L237">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L238">                                ! This specifies how bathymetry is specified:</span>
<span id="L239">                                !     file - read bathymetric information from the file</span>
<span id="L240">                                !       specified by (TOPO_FILE).</span>
<span id="L241">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L242">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L243">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L244">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L245">                                !       wall at the southern face.</span>
<span id="L246">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L247">                                !       profile in the meridional direction.</span>
<span id="L248">                                !     bbuilder - build topography from list of functions.</span>
<span id="L249">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L250">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L251">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L252">                                !       DOME sill-overflow test case.</span>
<span id="L253">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L254">                                !       ISOMIP test case.</span>
<span id="L255">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L256">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L257">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L258">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L259">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L260">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L261">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L262">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L263">                                !     USER - call a user modified routine.</span>
<span id="L264">MINIMUM_DEPTH = 0.5             !   [m] default = 0.0</span>
<span id="L265">                                ! The minimum depth of the ocean.</span>
<span id="L266">MAXIMUM_DEPTH = 6000.0          !   [m]</span>
<span id="L267">                                ! The maximum depth of the ocean.</span>
<span id="L268"></span>
<span id="L269">! === module MOM_open_boundary ===</span>
<span id="L270">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L271">! if any.</span>
<span id="L272">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L273">                                ! The number of open boundary segments.</span>
<span id="L274">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L275">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L276">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L277">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L278">                                ! A parameter that determines which set of channels are</span>
<span id="L279">                                ! restricted to specific  widths.  Options are:</span>
<span id="L280">                                !     none - All channels have the grid width.</span>
<span id="L281">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L282">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L283">                                !     list - Read the channel locations and widths from a</span>
<span id="L284">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L285">                                !       test case.</span>
<span id="L286">                                !     file - Read open face widths everywhere from a</span>
<span id="L287">                                !       NetCDF file on the model grid.</span>
<span id="L288">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L289">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L290">ROTATION = &quot;betaplane&quot;          ! default = &quot;2omegasinlat&quot;</span>
<span id="L291">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L292">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L293">                                !       times the sine of latitude.</span>
<span id="L294">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L295">                                !     USER - call a user modified routine.</span>
<span id="L296">F_0 = 7.59943E-05               !   [s-1] default = 0.0</span>
<span id="L297">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L298">BETA = 0.0                      !   [m-1 s-1] default = 0.0</span>
<span id="L299">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L300">BETA_LAT_REF = 0.0              !   [degrees] default = 0.0</span>
<span id="L301">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L302">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L303">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L304">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L305">                                ! arise at the tripolar fold.</span>
<span id="L306"></span>
<span id="L307">! === module MOM_verticalGrid ===</span>
<span id="L308">! Parameters providing information about the vertical grid.</span>
<span id="L309">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L310">                                ! The gravitational acceleration of the Earth.</span>
<span id="L311">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L312">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L313">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L314">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L315">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L316">                                ! If true, make the Boussinesq approximation.</span>
<span id="L317">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L318">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L319">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L320">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L321">NK = 63                         !   [nondim]</span>
<span id="L322">                                ! The number of model layers.</span>
<span id="L323">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L324">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L325">                                ! production is set to 0.</span>
<span id="L326"></span>
<span id="L327">! === module MOM_tracer_registry ===</span>
<span id="L328"></span>
<span id="L329">! === module MOM_EOS ===</span>
<span id="L330">EQN_OF_STATE = &quot;WRIGHT&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L331">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L332">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L333">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L334">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L335">USE_WRIGHT_2ND_DERIV_BUG = False !   [Boolean] default = False</span>
<span id="L336">                                ! If true, use a bug in the calculation of the second derivatives of density</span>
<span id="L337">                                ! with temperature and with temperature and pressure that causes some terms to</span>
<span id="L338">                                ! be only 2/3 of what they should be.</span>
<span id="L339">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L340">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L341">                                ! density.</span>
<span id="L342">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L343">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L344">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L345">                                ! &quot;TEOS10&quot;</span>
<span id="L346">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L347">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L348">                                ! P=0.</span>
<span id="L349">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L350">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L351">                                ! temperature with salinity.</span>
<span id="L352">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L353">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L354">                                ! temperature with pressure.</span>
<span id="L355">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L356">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L357">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L358">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L359">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L360">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L361">                                ! applied.</span>
<span id="L362"></span>
<span id="L363">! === module MOM_restart ===</span>
<span id="L364">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L365">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L366">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L367">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L368">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L369">                                ! The name-root of the restart file.</span>
<span id="L370">MAX_FIELDS = 100                ! default = 100</span>
<span id="L371">                                ! The maximum number of restart fields that can be used.</span>
<span id="L372">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L373">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L374">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L375">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L376">                                ! checksums will not match and cause crash.</span>
<span id="L377">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L378">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L379">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L380">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L381">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L382">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L383">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L384"></span>
<span id="L385">! === module MOM_tracer_flow_control ===</span>
<span id="L386">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L387">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L388">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L389">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L390">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L391">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L392">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L393">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L394">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L395">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L396">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L397">                                ! If true, use the MARBL tracer package.</span>
<span id="L398">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L399">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L400">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L401">                                ! If true, use the file dyes tracer package.</span>
<span id="L402">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L403">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L404">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L405">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L406">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L407">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L408">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L409">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L410">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L411">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L412">                                ! MOM_generic_tracer packages.</span>
<span id="L413">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L414">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L415">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L416">                                ! If true, use the boundary impulse tracer.</span>
<span id="L417">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L418">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L419">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L420">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L421"></span>
<span id="L422">! === module MOM_coord_initialization ===</span>
<span id="L423">COORD_CONFIG = &quot;file&quot;           ! default = &quot;none&quot;</span>
<span id="L424">                                ! This specifies how layers are to be defined:</span>
<span id="L425">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L426">                                !     file - read coordinate information from the file</span>
<span id="L427">                                !       specified by (COORD_FILE).</span>
<span id="L428">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L429">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L430">                                !     linear - linear based on interfaces not layers</span>
<span id="L431">                                !     layer_ref - linear based on layer densities</span>
<span id="L432">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L433">                                !     ts_range - use range of temperature and salinity</span>
<span id="L434">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L435">                                !       and GINT calculate internal densities.</span>
<span id="L436">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L437">                                !       density and GINT calculate internal densities.</span>
<span id="L438">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L439">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L440">                                !     USER - call a user modified routine.</span>
<span id="L441">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L442">                                ! The reduced gravity at the free surface.</span>
<span id="L443">COORD_FILE = &quot;../isopyc_coords.nc&quot; !</span>
<span id="L444">                                ! The file from which the coordinate densities are read.</span>
<span id="L445">COORD_VAR = &quot;Layer&quot;             ! default = &quot;Layer&quot;</span>
<span id="L446">                                ! The variable in COORD_FILE that is to be used for the coordinate densities.</span>
<span id="L447"></span>
<span id="L448">! === module MOM_state_initialization ===</span>
<span id="L449">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L450">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L451">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L452">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L453">INIT_LAYERS_FROM_Z_FILE = True  !   [Boolean] default = False</span>
<span id="L454">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L455">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L456"></span>
<span id="L457">! === module MOM_initialize_layers_from_Z ===</span>
<span id="L458">TEMP_SALT_Z_INIT_FILE = &quot;WOA_column.nc&quot; ! default = &quot;temp_salt_z.nc&quot;</span>
<span id="L459">                                ! The name of the z-space input file used to initialize temperatures (T) and</span>
<span id="L460">                                ! salinities (S). If T and S are not in the same file, TEMP_Z_INIT_FILE and</span>
<span id="L461">                                ! SALT_Z_INIT_FILE must be set.</span>
<span id="L462">TEMP_Z_INIT_FILE = &quot;WOA_column.nc&quot; ! default = &quot;WOA_column.nc&quot;</span>
<span id="L463">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L464">SALT_Z_INIT_FILE = &quot;WOA_column.nc&quot; ! default = &quot;WOA_column.nc&quot;</span>
<span id="L465">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L466">Z_INIT_FILE_PTEMP_VAR = &quot;PTEMP&quot; ! default = &quot;ptemp&quot;</span>
<span id="L467">                                ! The name of the potential temperature variable in TEMP_Z_INIT_FILE.</span>
<span id="L468">Z_INIT_FILE_SALT_VAR = &quot;SALT&quot;   ! default = &quot;salt&quot;</span>
<span id="L469">                                ! The name of the salinity variable in SALT_Z_INIT_FILE.</span>
<span id="L470">Z_INIT_HOMOGENIZE = True        !   [Boolean] default = False</span>
<span id="L471">                                ! If True, then horizontally homogenize the interpolated initial conditions.</span>
<span id="L472">Z_INIT_ALE_REMAPPING = False    !   [Boolean] default = False</span>
<span id="L473">                                ! If True, then remap straight to model coordinate from file.</span>
<span id="L474">Z_INIT_REMAPPING_SCHEME = &quot;PPM_IH4&quot; ! default = &quot;PPM_IH4&quot;</span>
<span id="L475">                                ! The remapping scheme to use if using Z_INIT_ALE_REMAPPING is True.</span>
<span id="L476">Z_INIT_REMAP_GENERAL = False    !   [Boolean] default = False</span>
<span id="L477">                                ! If false, only initializes to z* coordinates. If true, allows initialization</span>
<span id="L478">                                ! directly to general coordinates.</span>
<span id="L479">Z_INIT_REMAP_FULL_COLUMN = False !   [Boolean] default = False</span>
<span id="L480">                                ! If false, only reconstructs profiles for valid data points. If true, inserts</span>
<span id="L481">                                ! vanished layers below the valid data.</span>
<span id="L482">Z_INIT_REMAP_OLD_ALG = False    !   [Boolean] default = False</span>
<span id="L483">                                ! If false, uses the preferred remapping algorithm for initialization. If true,</span>
<span id="L484">                                ! use an older, less robust algorithm for remapping.</span>
<span id="L485">TEMP_SALT_INIT_VERTICAL_REMAP_ONLY = False !   [Boolean] default = False</span>
<span id="L486">                                ! If true, initial conditions are on the model horizontal grid. Extrapolation</span>
<span id="L487">                                ! over missing ocean values is done using an ICE-9 procedure with vertical ALE</span>
<span id="L488">                                ! remapping .</span>
<span id="L489">HOR_REGRID_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L490">                                ! The vintage of the order of arithmetic for horizontal regridding.  Dates</span>
<span id="L491">                                ! before 20190101 give the same answers as the code did in late 2018, while</span>
<span id="L492">                                ! later versions add parentheses for rotational symmetry.  Dates after 20230101</span>
<span id="L493">                                ! use reproducing sums for global averages.</span>
<span id="L494">ADJUST_THICKNESS = True         !   [Boolean] default = False</span>
<span id="L495">                                ! If true, all mass below the bottom removed if the topography is shallower than</span>
<span id="L496">                                ! the thickness input file would indicate.</span>
<span id="L497">THICKNESS_TOLERANCE = 0.1       !   [m] default = 0.1</span>
<span id="L498">                                ! A parameter that controls the tolerance when adjusting the thickness to fit</span>
<span id="L499">                                ! the bathymetry. Used when ADJUST_THICKNESS=True.</span>
<span id="L500">FIT_TO_TARGET_DENSITY_IC = True !   [Boolean] default = True</span>
<span id="L501">                                ! If true, all the interior layers are adjusted to their target densities using</span>
<span id="L502">                                ! mostly temperature This approach can be problematic, particularly in the high</span>
<span id="L503">                                ! latitudes.</span>
<span id="L504">Z_INIT_SEPARATE_MIXED_LAYER = False !   [Boolean] default = False</span>
<span id="L505">                                ! If true, distribute the topmost Z_INIT_HMIX_DEPTH of water over NKML layers,</span>
<span id="L506">                                ! and do not correct the density of the topmost NKML+NKBL layers.  Otherwise all</span>
<span id="L507">                                ! layers are initialized based on the depths of their target densities.</span>
<span id="L508">DENSITY_INTERP_TOLERANCE = 1.0E-10 !   [kg m-3] default = 1.0E-10</span>
<span id="L509">                                ! A small density tolerance used when finding depths in a density profile.</span>
<span id="L510">LAYER_Z_INIT_IC_EXTRAP_BUG = False !   [Boolean] default = False</span>
<span id="L511">                                ! If true use an expression with a vertical indexing bug for extrapolating the</span>
<span id="L512">                                ! densities at the bottom of unstable profiles from data when finding the</span>
<span id="L513">                                ! initial interface locations in layered mode from a dataset of T and S.</span>
<span id="L514">LAND_FILL_TEMP = 0.0            !   [degC] default = 0.0</span>
<span id="L515">                                ! A value to use to fill in ocean temperatures on land points.</span>
<span id="L516">LAND_FILL_SALIN = 35.0          !   [ppt] default = 35.0</span>
<span id="L517">                                ! A value to use to fill in ocean salinities on land points.</span>
<span id="L518">HORIZ_INTERP_TOL_TEMP = 0.001   !   [degC] default = 0.001</span>
<span id="L519">                                ! The tolerance in temperature changes between iterations when interpolating</span>
<span id="L520">                                ! from an input dataset using horiz_interp_and_extrap_tracer.  This routine</span>
<span id="L521">                                ! converges slowly, so an overly small tolerance can get expensive.</span>
<span id="L522">HORIZ_INTERP_TOL_SALIN = 0.001  !   [ppt] default = 0.001</span>
<span id="L523">                                ! The tolerance in salinity changes between iterations when interpolating from</span>
<span id="L524">                                ! an input dataset using horiz_interp_and_extrap_tracer.  This routine converges</span>
<span id="L525">                                ! slowly, so an overly small tolerance can get expensive.</span>
<span id="L526"></span>
<span id="L527">! === module determine_temperature ===</span>
<span id="L528">DETERMINE_TEMP_ADJUST_T_AND_S = False !   [Boolean] default = False</span>
<span id="L529">                                ! If true, simltaneously adjust the estimates of the temperature and salinity</span>
<span id="L530">                                ! based on the ratio of the thermal and haline coefficients.  Otherwise try to</span>
<span id="L531">                                ! match the density by only adjusting temperatures within a maximum range before</span>
<span id="L532">                                ! revising estimates of the salinity.</span>
<span id="L533">DETERMINE_TEMP_CONVERGENCE_BUG = False !   [Boolean] default = False</span>
<span id="L534">                                ! If true, use layout-dependent tests on the changes in temperature and salinity</span>
<span id="L535">                                ! to determine when the iterations have converged when</span>
<span id="L536">                                ! DETERMINE_TEMP_ADJUST_T_AND_S is false.  For realistic equations of state and</span>
<span id="L537">                                ! the default values of the various tolerances, this bug does not impact the</span>
<span id="L538">                                ! solutions.</span>
<span id="L539">DETERMINE_TEMP_T_MIN = -2.0     !   [degC] default = -2.0</span>
<span id="L540">                                ! The minimum temperature that can be found by determine_temperature.</span>
<span id="L541">DETERMINE_TEMP_T_MAX = 31.0     !   [degC] default = 31.0</span>
<span id="L542">                                ! The maximum temperature that can be found by determine_temperature.</span>
<span id="L543">DETERMINE_TEMP_S_MIN = 0.5      !   [ppt] default = 0.5</span>
<span id="L544">                                ! The minimum salinity that can be found by determine_temperature.</span>
<span id="L545">DETERMINE_TEMP_S_MAX = 65.0     !   [ppt] default = 65.0</span>
<span id="L546">                                ! The maximum salinity that can be found by determine_temperature.</span>
<span id="L547">DETERMINE_TEMP_RHO_TOLERANCE = 1.0E-04 !   [kg m-3] default = 1.0E-04</span>
<span id="L548">                                ! The convergence tolerance for density in determine_temperature.</span>
<span id="L549">DETERMINE_TEMP_T_ADJ_RANGE = 1.0 !   [degC] default = 1.0</span>
<span id="L550">                                ! The maximum amount by which the initial layer temperatures can be modified in</span>
<span id="L551">                                ! determine_temperature.</span>
<span id="L552">DETERMINE_TEMP_S_ADJ_RANGE = 0.5 !   [ppt] default = 0.5</span>
<span id="L553">                                ! The maximum amount by which the initial layer salinities can be modified in</span>
<span id="L554">                                ! determine_temperature.</span>
<span id="L555">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L556">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L557">                                ! surface pressure is applied.</span>
<span id="L558">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L559">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L560">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L561">                                ! read from file.</span>
<span id="L562">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L563">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L564">                                ! run:</span>
<span id="L565">                                !     file - read velocities from the file specified</span>
<span id="L566">                                !       by (VELOCITY_FILE).</span>
<span id="L567">                                !     zero - the fluid is initially at rest.</span>
<span id="L568">                                !     uniform - the flow is uniform (determined by</span>
<span id="L569">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L570">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L571">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L572">                                !     USER - call a user modified routine.</span>
<span id="L573">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L574">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L575">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L576">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L577">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L578"></span>
<span id="L579">! === module MOM_diag_mediator ===</span>
<span id="L580">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L581">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L582">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L583">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L584">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L585">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L586">                                ! false.</span>
<span id="L587">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L588">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L589">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L590">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L591">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L592">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L593">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L594">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L595">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L596">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L597">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L598">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L599">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L600">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L601">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L602">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L603">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L604">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L605">                                ! be included in a diag_table.</span>
<span id="L606">DIAG_COORD_DEF_Z = &quot;WOA09&quot;      ! default = &quot;WOA09&quot;</span>
<span id="L607">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L608">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L609">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L610">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L611">                                !                the filename and variable name, separated</span>
<span id="L612">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L613">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L614">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L615">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L616">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L617">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L618">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L619">                                !                the filename and two variable names, separated</span>
<span id="L620">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L621">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L622">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L623">                                !                the filename and two 3D variable names, separated</span>
<span id="L624">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L625">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L626">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L627">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L628">                                !                the filename and three variable names, separated</span>
<span id="L629">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L630">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L631">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L632">                                !                Map typically contains integer values, but it can</span>
<span id="L633">                                !                contain real values, I+w, which imply using</span>
<span id="L634">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L635">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L636">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L637"></span>
<span id="L638">! === module MOM_MEKE ===</span>
<span id="L639">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L640">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L641">                                ! kinetic energy budget.</span>
<span id="L642"></span>
<span id="L643">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L644">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L645">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L646">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L647">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L648">                                ! file.</span>
<span id="L649">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L650">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L651">                                ! thickness diffusivity.</span>
<span id="L652">RESOLN_SCALED_KH = False        !   [Boolean] default = False</span>
<span id="L653">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L654">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L655">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L656">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L657">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L658">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L659">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L660">RESOLN_SCALED_KHTH = False      !   [Boolean] default = False</span>
<span id="L661">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L662">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L663">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L664">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L665">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L666">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L667">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L668">                                ! wave for calculating the resolution fn.</span>
<span id="L669">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L670">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L671">                                ! structure.</span>
<span id="L672">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L673">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L674">                                ! that BS_EBT_power=0</span>
<span id="L675">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L676">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L677">                                ! thickness diffusivity.</span>
<span id="L678">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L679">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L680">                                ! of thickness diffusivity.</span>
<span id="L681">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L682">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L683">                                ! tracer diffusivity.</span>
<span id="L684">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L685">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L686">                                ! of tracer diffusivity.</span>
<span id="L687">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L688">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L689">                                ! diffusivity in the GL90 scheme.</span>
<span id="L690">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L691">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L692">                                ! diffusivity in the GL90 scheme.</span>
<span id="L693">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L694">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L695">                                ! diffusivity</span>
<span id="L696">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L697">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L698">                                ! diffusivity</span>
<span id="L699">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L700">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L701">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L702">                                ! should be necessary.</span>
<span id="L703">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L704">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L705">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L706">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L707">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L708">                                ! code.</span>
<span id="L709">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L710">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L711">                                ! &amp; S into thin layers.</span>
<span id="L712">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L713">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L714"></span>
<span id="L715">! === module MOM_set_visc ===</span>
<span id="L716">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L717">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L718">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L719">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L720">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L721">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L722">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L723">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L724">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L725">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L726">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L727">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L728">                                ! layer is HBBL.</span>
<span id="L729">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L730">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L731">                                ! fraction of the bottom it overlies.</span>
<span id="L732">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L733">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L734">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L735">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L736">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L737">                                ! thickness for viscosity.</span>
<span id="L738">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L739">                                ! The rotation rate of the earth.</span>
<span id="L740">HBBL = 10.0                     !   [m]</span>
<span id="L741">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L742">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L743">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L744">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L745">CDRAG = 0.0                     !   [nondim] default = 0.003</span>
<span id="L746">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L747">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L748">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L749">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L750">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L751">                                ! and LINEAR_DRAG is false.</span>
<span id="L752">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L753">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L754">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L755">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L756">                                ! defined.</span>
<span id="L757">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L758">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L759">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L760">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L761">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L762">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L763">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L764">                                ! near-bottom viscosity.</span>
<span id="L765">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L766">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L767">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L768">                                ! viscosity.</span>
<span id="L769">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L770">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L771">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L772">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L773">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L774">                                ! m2 s-1, may be used.</span>
<span id="L775">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L776">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L777">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L778">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L779">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L780">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L781">                                ! the bottom layer feels the intended drag.</span>
<span id="L782"></span>
<span id="L783">! === module MOM_thickness_diffuse ===</span>
<span id="L784">KHTH = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L785">                                ! The background horizontal thickness diffusivity.</span>
<span id="L786">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L787">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L788">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L789">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L790">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L791">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L792">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L793">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L794">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L795">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L796">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L797">                                ! models.</span>
<span id="L798">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L799">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L800">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L801">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L802">                                ! are scaled back proportionately.</span>
<span id="L803">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L804">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L805">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L806">                                ! the layer density structure).</span>
<span id="L807">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L808">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L809">                                ! horizontally smooth jagged layers.</span>
<span id="L810">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L811">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L812">                                ! scaled away.</span>
<span id="L813">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L814">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L815">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L816">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L817">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L818">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L819">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L820">                                ! streamfunction for the GM source term.</span>
<span id="L821">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L822">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L823">                                ! (Marshall et al., 2012).</span>
<span id="L824">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L825">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L826">                                ! McWilliams parameterization.</span>
<span id="L827">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L828">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L829">                                ! sign, for legacy reproducibility.</span>
<span id="L830">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L831">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L832">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L833">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L834"></span>
<span id="L835">! === module MOM_dynamics_unsplit ===</span>
<span id="L836">UNSPLIT_DT_VISC_BUG = False     !   [Boolean] default = False</span>
<span id="L837">                                ! If false, use the correct timestep in the viscous terms applied in the first</span>
<span id="L838">                                ! predictor step with the unsplit time stepping scheme, and in the calculation</span>
<span id="L839">                                ! of the turbulent mixed layer properties for viscosity with unsplit or</span>
<span id="L840">                                ! unsplit_RK2.  If true, an older incorrect value is used.</span>
<span id="L841">TIDES = False                   !   [Boolean] default = False</span>
<span id="L842">                                ! If true, apply tidal momentum forcing.</span>
<span id="L843">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L844">                                ! If true, calculate self-attraction and loading.</span>
<span id="L845"></span>
<span id="L846">! === module MOM_continuity_PPM ===</span>
<span id="L847">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L848">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L849">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L850">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L851">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L852">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L853">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L854">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L855">                                ! of accuracy of the dynamic core.</span>
<span id="L856">UPWIND_1ST_CONTINUITY = True    !   [Boolean] default = False</span>
<span id="L857">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L858">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L859">                                ! mode where its minimal stencil is useful.</span>
<span id="L860">ETA_TOLERANCE = 3.15E-09        !   [m] default = 3.15E-09</span>
<span id="L861">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L862">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L863">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L864">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L865">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L866">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L867">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L868">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L869">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L870">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L871">                                ! 0.5.</span>
<span id="L872">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L873">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L874">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L875">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L876">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L877">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L878">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L879">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L880">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L881">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L882">                                ! viscous columns.</span>
<span id="L883">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L884">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L885">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L886"></span>
<span id="L887">! === module MOM_CoriolisAdv ===</span>
<span id="L888">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L889">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L890">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L891">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L892">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L893">CORIOLIS_EN_DIS = True          !   [Boolean] default = False</span>
<span id="L894">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L895">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L896">                                ! used.</span>
<span id="L897">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L898">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L899">                                ! values are:</span>
<span id="L900">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L901">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L902">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L903">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L904">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L905">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L906">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L907">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L908">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L909">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L910">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L911">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L912">                                ! option is always effectively false with CORIOLIS_EN_DIS defined and</span>
<span id="L913">                                ! CORIOLIS_SCHEME set to SADOURNY75_ENERGY.</span>
<span id="L914">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L915">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L916">                                ! energy gradient. Valid values are:</span>
<span id="L917">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L918">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L919">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L920">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L921">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L922"></span>
<span id="L923">! === module MOM_PressureForce ===</span>
<span id="L924">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L925">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L926">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L927">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L928">                                ! al., O. Mod. (2008).</span>
<span id="L929"></span>
<span id="L930">! === module MOM_PressureForce_FV ===</span>
<span id="L931">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L932">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L933">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L934">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L935">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L936">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L937">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L938">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L939">                                ! Boussinesq mode.</span>
<span id="L940">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L941">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L942">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L943">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L944">                                ! pressure.</span>
<span id="L945">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L946">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L947">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L948">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L949">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L950">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L951">                                ! pressure gradient calculations.</span>
<span id="L952">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L953">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L954">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L955">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L956">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L957">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L958">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L959">                                ! pressure correction.</span>
<span id="L960">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L961">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L962">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L963">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L964">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L965">                                ! inaccurate way. This is not recommended.</span>
<span id="L966">RECONSTRUCT_FOR_PRESSURE = False !   [Boolean] default = False</span>
<span id="L967">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L968">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L969">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L970">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L971">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L972">                                ! pressure gradient calculation.</span>
<span id="L973">                                !  0: PCM or no reconstruction.</span>
<span id="L974">                                !  1: PLM reconstruction.</span>
<span id="L975">                                !  2: PPM reconstruction.</span>
<span id="L976">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L977">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L978">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L979">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L980">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L981">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L982"></span>
<span id="L983">! === module MOM_Zanna_Bolton ===</span>
<span id="L984">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L985">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L986">                                ! mesoscale eddies.</span>
<span id="L987"></span>
<span id="L988">! === module MOM_hor_visc ===</span>
<span id="L989">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L990">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L991">                                ! Leith)</span>
<span id="L992">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L993">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L994">                                ! currently only works with split mode.</span>
<span id="L995">LAPLACIAN = False               !   [Boolean] default = False</span>
<span id="L996">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L997">BIHARMONIC = False              !   [Boolean] default = True</span>
<span id="L998">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L999">                                ! LAPLACIAN.</span>
<span id="L1000">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1001">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1002">                                ! harmonic backscatter.</span>
<span id="L1003">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1004">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1005">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1006">                                ! outside of the domain.</span>
<span id="L1007">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1008">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1009">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1010">                                ! recommended.</span>
<span id="L1011"></span>
<span id="L1012">! === module MOM_vert_friction ===</span>
<span id="L1013">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1014">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1015">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1016">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1017">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1018">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1019">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1020">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1021">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1022">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1023">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1024">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1025">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1026">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1027">                                ! of the ocean in a column.</span>
<span id="L1028">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1029">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1030">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1031">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1032">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1033">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1034">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1035">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1036">HARMONIC_VISC = True            !   [Boolean] default = False</span>
<span id="L1037">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1038">                                ! viscosity.</span>
<span id="L1039">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1040">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1041">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1042">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1043">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1044">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1045">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1046">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1047">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1048">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1049">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1050">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1051">                                ! default is CFL_TRUNCATE.</span>
<span id="L1052">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1053">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1054">                                ! the run.</span>
<span id="L1055">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1056">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1057">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1058">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1059">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1060">VEL_UNDERFLOW = 1.0E-30         !   [m s-1] default = 0.0</span>
<span id="L1061">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1062">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1063">                                ! divided by the age of the universe.</span>
<span id="L1064"></span>
<span id="L1065">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1066">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L1067">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1068">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1069">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1070"></span>
<span id="L1071">! === module MOM_diagnostics ===</span>
<span id="L1072">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1073">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1074">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1075">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1076">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1077">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1078">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1079">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1080">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1081">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1082">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L1083">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1084">                                ! starting point for iterations.</span>
<span id="L1085">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1086">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1087">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1088">                                ! this option to false.</span>
<span id="L1089"></span>
<span id="L1090">! === module MOM_diabatic_driver ===</span>
<span id="L1091">! The following parameters are used for diabatic processes.</span>
<span id="L1092">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1093">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1094">                                ! and is needed to avoid change in answers.</span>
<span id="L1095">ENERGETICS_SFC_PBL = False      !   [Boolean] default = False</span>
<span id="L1096">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1097">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1098">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1099">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1100">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1101">ML_MIX_FIRST = 0.0              !   [nondim] default = 0.0</span>
<span id="L1102">                                ! The fraction of the mixed layer mixing that is applied before interior</span>
<span id="L1103">                                ! diapycnal mixing.  0 by default.</span>
<span id="L1104">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1105">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1106">                                ! internal tide energy density.</span>
<span id="L1107">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1108">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1109">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1110">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1111">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1112">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1113">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1114">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1115">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1116">                                ! updated state.</span>
<span id="L1117">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1118">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1119">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1120">KD_MIN_TR = 2.0E-06             !   [m2 s-1] default = 2.0E-06</span>
<span id="L1121">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1122">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1123">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1124">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1125">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1126">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1127">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1128">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1129">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1130">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1131">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1132">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1133">                                ! scale.</span>
<span id="L1134">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1135">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1136">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1137">                                ! through the column.</span>
<span id="L1138">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1139">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1140">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1141">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1142">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1143">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1144">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1145">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1146">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1147">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1148">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1149">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1150">                                ! base of the mixed layer.</span>
<span id="L1151"></span>
<span id="L1152">! === module MOM_CVMix_KPP ===</span>
<span id="L1153">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1154">! See http://cvmix.github.io/</span>
<span id="L1155">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1156">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1157">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1158"></span>
<span id="L1159">! === module MOM_CVMix_conv ===</span>
<span id="L1160">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1161">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1162">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1163">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1164">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1165"></span>
<span id="L1166">! === module MOM_entrain_diffusive ===</span>
<span id="L1167">MAX_ENT_IT = 20                 ! default = 5</span>
<span id="L1168">                                ! The maximum number of iterations that may be used to calculate the interior</span>
<span id="L1169">                                ! diapycnal entrainment.</span>
<span id="L1170">TOLERANCE_ENT = 1.0E-05         !   [m] default = 2.683281572999748E-05</span>
<span id="L1171">                                ! The tolerance with which to solve for entrainment values.</span>
<span id="L1172">ENTRAIN_DIFFUSIVE_MAX_ENT = 1.0E+04 !   [m] default = 1.0E+04</span>
<span id="L1173">                                ! A large ceiling on the maximum permitted amount of entrainment across each</span>
<span id="L1174">                                ! interface between the mixed and buffer layers within a timestep.</span>
<span id="L1175"></span>
<span id="L1176">! === module MOM_set_diffusivity ===</span>
<span id="L1177">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1178">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1179">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1180">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1181">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1182">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1183">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1184">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1185">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1186">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1187"></span>
<span id="L1188">! === module MOM_tidal_mixing ===</span>
<span id="L1189">! Vertical Tidal Mixing Parameterization</span>
<span id="L1190">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1191">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1192">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1193">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1194">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1195">ML_RADIATION = True             !   [Boolean] default = False</span>
<span id="L1196">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1197">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1198">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1199">ML_RAD_EFOLD_COEFF = 0.2        !   [nondim] default = 0.2</span>
<span id="L1200">                                ! A coefficient that is used to scale the penetration depth for turbulence below</span>
<span id="L1201">                                ! the base of the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1202">ML_RAD_BUG = False              !   [Boolean] default = False</span>
<span id="L1203">                                ! If true use code with a bug that reduces the energy available in the</span>
<span id="L1204">                                ! transition layer by a factor of the inverse of the energy deposition</span>
<span id="L1205">                                ! lenthscale (in m).</span>
<span id="L1206">ML_RAD_KD_MAX = 0.001           !   [m2 s-1] default = 0.001</span>
<span id="L1207">                                ! The maximum diapycnal diffusivity due to turbulence radiated from the base of</span>
<span id="L1208">                                ! the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1209">ML_RAD_COEFF = 0.2              !   [nondim] default = 0.2</span>
<span id="L1210">                                ! The coefficient which scales MSTAR*USTAR^3 to obtain the energy available for</span>
<span id="L1211">                                ! mixing below the base of the mixed layer. This is only used if ML_RADIATION is</span>
<span id="L1212">                                ! true.</span>
<span id="L1213">ML_RAD_APPLY_TKE_DECAY = True   !   [Boolean] default = True</span>
<span id="L1214">                                ! If true, apply the same exponential decay to ML_rad as is applied to the other</span>
<span id="L1215">                                ! surface sources of TKE in the mixed layer code. This is only used if</span>
<span id="L1216">                                ! ML_RADIATION is true.</span>
<span id="L1217">MSTAR = 1.2                     !   [nondim] default = 1.2</span>
<span id="L1218">                                ! The ratio of the friction velocity cubed to the TKE input to the mixed layer.</span>
<span id="L1219">TKE_DECAY = 10.0                !   [nondim] default = 2.5</span>
<span id="L1220">                                ! The ratio of the natural Ekman depth to the TKE decay scale.</span>
<span id="L1221">ML_OMEGA_FRAC = 1.0             !   [nondim] default = 0.0</span>
<span id="L1222">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L1223">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L1224">                                ! of*4*omega^2).</span>
<span id="L1225">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1226">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1227">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1228">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1229">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1230">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1231">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1232">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1233">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1234">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1235">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1236">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1237">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1238">                                ! scheme.</span>
<span id="L1239">DRAG_DIFFUSIVITY_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1240">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1241">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1242">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1243">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1244">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1245">                                ! boundary layer density.</span>
<span id="L1246">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1247">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1248">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1249">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1250"></span>
<span id="L1251">! === module MOM_bkgnd_mixing ===</span>
<span id="L1252">! Adding static vertical background mixing coefficients</span>
<span id="L1253">KD = 2.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1254">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1255">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1256">KD_MIN = 2.0E-06                !   [m2 s-1] default = 2.0E-07</span>
<span id="L1257">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1258">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1259">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1260">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1261">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1262">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1263">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1264">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1265">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1266">                                ! into viscosities.</span>
<span id="L1267">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1268">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1269">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1270">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1271">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1272">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1273">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1274">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1275">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1276">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1277">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1278">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1279">                                ! or scaling.</span>
<span id="L1280">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1281">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1282">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1283">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1284">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1285">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1286">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1287">                                ! = A + B*N.</span>
<span id="L1288">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1289">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1290">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1291">                                ! = A + B*N</span>
<span id="L1292">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1293">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1294">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1295">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1296">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1297"></span>
<span id="L1298">! === module MOM_kappa_shear ===</span>
<span id="L1299">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1300">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1301">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1302">                                ! parameterization.</span>
<span id="L1303">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L1304">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1305">                                ! (i.e., the vorticity points).</span>
<span id="L1306">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1307">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1308">                                ! tracer points in the kappa shear solver.</span>
<span id="L1309">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L1310">                                ! The critical Richardson number for shear mixing.</span>
<span id="L1311">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L1312">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L1313">                                ! values in the range of 0.085-0.089.</span>
<span id="L1314">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L1315">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L1316">                                ! number driven mixing.</span>
<span id="L1317">KD_KAPPA_SHEAR_0 = 2.0E-05      !   [m2 s-1] default = 2.0E-05</span>
<span id="L1318">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L1319">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L1320">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L1321">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1322">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1323">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1324">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1325">KD_TRUNC_KAPPA_SHEAR = 2.0E-07  !   [m2 s-1] default = 2.0E-07</span>
<span id="L1326">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L1327">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L1328">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L1329">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L1330">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L1331">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L1332">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L1333">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L1334">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L1335">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L1336">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L1337">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L1338">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L1339">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L1340">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1341">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L1342">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L1343">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1344">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1345">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1346">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1347">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1348">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L1349">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L1350">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L1351">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L1352">                                ! errors than this.</span>
<span id="L1353">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1354">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1355">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1356">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L1357">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L1358">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L1359">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1360">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L1361">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L1362">                                ! time-averaged diffusivity.</span>
<span id="L1363">PRANDTL_TURB = 0.0              !   [nondim] default = 1.0</span>
<span id="L1364">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L1365">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L1366">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L1367">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L1368">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L1369">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L1370">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L1371">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L1372">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L1373">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L1374">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L1375">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L1376">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L1377">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L1378">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L1379">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L1380">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L1381">                                ! less restrictive check.</span>
<span id="L1382">KAPPA_SHEAR_MERGE_ML = True     !   [Boolean] default = True</span>
<span id="L1383">                                ! If true, combine the mixed layers together before solving the kappa-shear</span>
<span id="L1384">                                ! equations.</span>
<span id="L1385"></span>
<span id="L1386">! === module MOM_CVMix_shear ===</span>
<span id="L1387">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1388">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1389">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1390">                                ! parameterization.</span>
<span id="L1391">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1392">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1393">                                ! parameterization.</span>
<span id="L1394"></span>
<span id="L1395">! === module MOM_CVMix_ddiff ===</span>
<span id="L1396">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1397">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1398">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1399">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1400">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1401"></span>
<span id="L1402">! === module MOM_diabatic_aux ===</span>
<span id="L1403">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1404">RECLAIM_FRAZIL = False          !   [Boolean] default = True</span>
<span id="L1405">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1406">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1407">                                ! is above the freezing point.</span>
<span id="L1408">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1409">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1410">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1411">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1412">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1413">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1414">                                ! cavities.</span>
<span id="L1415">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1416">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1417">VAR_PEN_SW = True               !   [Boolean] default = False</span>
<span id="L1418">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1419">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1420">CHL_FROM_FILE = True            !   [Boolean] default = True</span>
<span id="L1421">                                ! If true, chl_a is read from a file.</span>
<span id="L1422">CHL_FILE = &quot;forcing_monthly.nc&quot; !</span>
<span id="L1423">                                ! CHL_FILE is the file containing chl_a concentrations in the variable CHL_A. It</span>
<span id="L1424">                                ! is used when VAR_PEN_SW and CHL_FROM_FILE are true.</span>
<span id="L1425">CHL_VARNAME = &quot;CHL_A&quot;           ! default = &quot;CHL_A&quot;</span>
<span id="L1426">                                ! Name of CHL_A variable in CHL_FILE.</span>
<span id="L1427"></span>
<span id="L1428">! === module MOM_mixed_layer ===</span>
<span id="L1429">NSTAR = 0.15                    !   [nondim] default = 0.15</span>
<span id="L1430">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L1431">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L1432">                                ! positive.</span>
<span id="L1433">BULK_RI_ML = 0.05               !   [nondim]</span>
<span id="L1434">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L1435">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L1436">ABSORB_ALL_SW = True            !   [Boolean] default = False</span>
<span id="L1437">                                ! If true,  all shortwave radiation is absorbed by the ocean, instead of passing</span>
<span id="L1438">                                ! through to the bottom mud.</span>
<span id="L1439">NSTAR2 = 0.15                   !   [nondim] default = 0.15</span>
<span id="L1440">                                ! The portion of any potential energy released by convective adjustment that is</span>
<span id="L1441">                                ! available to drive entrainment at the base of mixed layer. By default</span>
<span id="L1442">                                ! NSTAR2=NSTAR.</span>
<span id="L1443">BULK_RI_CONVECTIVE = 0.05       !   [nondim] default = 0.05</span>
<span id="L1444">                                ! The efficiency with which convectively released mean kinetic energy is</span>
<span id="L1445">                                ! converted to turbulent kinetic energy.  By default</span>
<span id="L1446">                                ! BULK_RI_CONVECTIVE=BULK_RI_ML.</span>
<span id="L1447">HMIX_MIN = 2.0                  !   [m] default = 0.0</span>
<span id="L1448">                                ! The minimum mixed layer depth if the mixed layer depth is determined</span>
<span id="L1449">                                ! dynamically.</span>
<span id="L1450">MECH_TKE_FLOOR = 1.0E-150       !   [m3 s-2] default = 1.0E-150</span>
<span id="L1451">                                ! A tiny floor on the amount of turbulent kinetic energy that is used when the</span>
<span id="L1452">                                ! mixed layer does not yet contain HMIX_MIN fluid.  The default is so small that</span>
<span id="L1453">                                ! its actual value is irrelevant, so long as it is greater than 0.</span>
<span id="L1454">LIMIT_BUFFER_DETRAIN = False    !   [Boolean] default = False</span>
<span id="L1455">                                ! If true, limit the detrainment from the buffer layers to not be too different</span>
<span id="L1456">                                ! from the neighbors.</span>
<span id="L1457">ALLOWED_DETRAIN_TEMP_CHG = 0.5  !   [K] default = 0.5</span>
<span id="L1458">                                ! The amount by which temperature is allowed to exceed previous values during</span>
<span id="L1459">                                ! detrainment.</span>
<span id="L1460">ALLOWED_DETRAIN_SALT_CHG = 0.1  !   [ppt] default = 0.1</span>
<span id="L1461">                                ! The amount by which salinity is allowed to exceed previous values during</span>
<span id="L1462">                                ! detrainment.</span>
<span id="L1463">ML_DT_DS_WEIGHT = 6.0           !   [degC ppt-1] default = 6.0</span>
<span id="L1464">                                ! When forced to extrapolate T &amp; S to match the layer densities, this factor (in</span>
<span id="L1465">                                ! deg C / PSU) is combined with the derivatives of density with T &amp; S to</span>
<span id="L1466">                                ! determine what direction is orthogonal to density contours. It should be a</span>
<span id="L1467">                                ! typical value of (dR/dS) / (dR/dT) in oceanic profiles.</span>
<span id="L1468">BUFFER_LAYER_EXTRAP_LIMIT = -1.0 !   [nondim] default = -1.0</span>
<span id="L1469">                                ! A limit on the density range over which extrapolation can occur when</span>
<span id="L1470">                                ! detraining from the buffer layers, relative to the density range within the</span>
<span id="L1471">                                ! mixed and buffer layers, when the detrainment is going into the lightest</span>
<span id="L1472">                                ! interior layer, nondimensional, or a negative value not to apply this limit.</span>
<span id="L1473">BUFFER_LAYER_HMIN_THICK = 5.0   !   [m] default = 5.0</span>
<span id="L1474">                                ! The minimum buffer layer thickness when the mixed layer is very thick.</span>
<span id="L1475">BUFFER_LAYER_HMIN_REL = 0.05    !   [nondim] default = 0.05</span>
<span id="L1476">                                ! The minimum buffer layer thickness relative to the combined mixed land buffer</span>
<span id="L1477">                                ! ayer thicknesses when they are thin.</span>
<span id="L1478">BUFFER_LAY_DETRAIN_TIME = 1.44E+04 !   [s] default = 1.44E+04</span>
<span id="L1479">                                ! A timescale that characterizes buffer layer detrainment events.</span>
<span id="L1480">BUFFER_SPLIT_RHO_TOL = 0.1      !   [nondim] default = 0.1</span>
<span id="L1481">                                ! The fractional tolerance for matching layer target densities when splitting</span>
<span id="L1482">                                ! layers to deal with massive interior layers that are lighter than one of the</span>
<span id="L1483">                                ! mixed or buffer layers.</span>
<span id="L1484">DEPTH_LIMIT_FLUXES = 0.1        !   [m] default = 0.2</span>
<span id="L1485">                                ! The surface fluxes are scaled away when the total ocean depth is less than</span>
<span id="L1486">                                ! DEPTH_LIMIT_FLUXES.</span>
<span id="L1487">ML_RESORT = False               !   [Boolean] default = False</span>
<span id="L1488">                                ! If true, resort the topmost layers by potential density before the mixed layer</span>
<span id="L1489">                                ! calculations.</span>
<span id="L1490">BML_USTAR_MIN = 1.45842E-18     !   [m s-1] default = 1.45842E-18</span>
<span id="L1491">                                ! The minimum value of ustar that should be used by the bulk mixed layer model</span>
<span id="L1492">                                ! in setting vertical TKE decay scales. This must be greater than 0.</span>
<span id="L1493">BML_NONBOUSINESQ = False        !   [Boolean] default = False</span>
<span id="L1494">                                ! If true, use non-Boussinesq expressions for the energetic calculations used in</span>
<span id="L1495">                                ! the bulk mixed layer calculations.</span>
<span id="L1496">RESOLVE_EKMAN = False           !   [Boolean] default = False</span>
<span id="L1497">                                ! If true, the NKML&gt;1 layers in the mixed layer are chosen to optimally</span>
<span id="L1498">                                ! represent the impact of the Ekman transport on the mixed layer TKE budget.</span>
<span id="L1499">                                ! Otherwise, the sublayers are distributed uniformly through the mixed layer.</span>
<span id="L1500">CORRECT_ABSORPTION_DEPTH = True !   [Boolean] default = False</span>
<span id="L1501">                                ! If true, the average depth at which penetrating shortwave radiation is</span>
<span id="L1502">                                ! absorbed is adjusted to match the average heating depth of an exponential</span>
<span id="L1503">                                ! profile by moving some of the heating upward in the water column.</span>
<span id="L1504">DO_RIVERMIX = False             !   [Boolean] default = False</span>
<span id="L1505">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L1506">                                ! down to RIVERMIX_DEPTH, if the ocean is that deep.</span>
<span id="L1507">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1508">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1509">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1510">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1511">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1512">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1513">BULKML_CONV_MOMENTUM_BUG = False !   [Boolean] default = False</span>
<span id="L1514">                                ! If true, use code with a bug that causes a loss of momentum conservation</span>
<span id="L1515">                                ! during mixedlayer convection.</span>
<span id="L1516"></span>
<span id="L1517">! === module MOM_regularize_layers ===</span>
<span id="L1518">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L1519">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L1520">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L1521"></span>
<span id="L1522">! === module MOM_opacity ===</span>
<span id="L1523">OPACITY_SCHEME = &quot;MANIZZA_05&quot;   ! default = &quot;MANIZZA_05&quot;</span>
<span id="L1524">                                ! This character string specifies how chlorophyll concentrations are translated</span>
<span id="L1525">                                ! into opacities. Currently valid options include:</span>
<span id="L1526">                                !        MANIZZA_05 - Use Manizza et al., GRL, 2005.</span>
<span id="L1527">                                !        MOREL_88 - Use Morel, JGR, 1988.</span>
<span id="L1528">                                !        OHLMANN_03 - Use Ohlmann, J Clim, 2003. (only use if dz(1)&gt;2.0m)</span>
<span id="L1529">BLUE_FRAC_SW = 0.5              !   [nondim] default = 0.5</span>
<span id="L1530">                                ! The fraction of the penetrating shortwave radiation that is in the blue band.</span>
<span id="L1531">PEN_SW_NBANDS = 3               ! default = 1</span>
<span id="L1532">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L1533">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L1534">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L1535">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1536">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1537">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L1538">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L1539">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L1540">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L1541">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L1542">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L1543">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L1544">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L1545">OPACITY_VALUES_MANIZZA = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 !   [m-1] default = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0</span>
<span id="L1546">                                ! Pairs of opacity coefficients for blue, red and near-infrared radiation with</span>
<span id="L1547">                                ! parameterizations following the functional form from Manizza et al., GRL 2005,</span>
<span id="L1548">                                ! namely in the form opacity = coef_1 + coef_2 * chl**pow for each band.</span>
<span id="L1549">                                ! Although coefficients are set for 3 bands, more or less bands may actually be</span>
<span id="L1550">                                ! used, with extra bands following the same properties as band 3.</span>
<span id="L1551">CHOROPHYLL_POWER_MANIZZA = 0.674, 0.629, 0.0 !   [nondim] default = 0.674, 0.629, 0.0</span>
<span id="L1552">                                ! Powers of chlorophyll for blue, red and near-infrared radiation bands in</span>
<span id="L1553">                                ! expressions for opacity of the form opacity = coef_1 + coef_2 * chl**pow.</span>
<span id="L1554">OPACITY_BAND_WAVELENGTHS = 0.0, 550.0, 700.0, 2800.0 !   [nm] default = 0.0, 550.0, 700.0, 2800.0</span>
<span id="L1555">                                ! The bounding wavelengths for the various bands of shortwave radiation, with</span>
<span id="L1556">                                ! defaults that depend on the setting for OPACITY_SCHEME.</span>
<span id="L1557">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L1558">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L1559">                                ! muddy water.</span>
<span id="L1560"></span>
<span id="L1561">! === module MOM_tracer_advect ===</span>
<span id="L1562">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L1563">                                ! The horizontal transport scheme for tracers:</span>
<span id="L1564">                                !   PLM    - Piecewise Linear Method</span>
<span id="L1565">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L1566">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L1567"></span>
<span id="L1568">! === module MOM_tracer_hor_diff ===</span>
<span id="L1569">KHTR = 600.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1570">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L1571">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1572">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L1573">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1574">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L1575">                                ! activate.</span>
<span id="L1576">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L1577">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L1578">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L1579">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L1580">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L1581">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L1582">                                ! tracers to thickness mixing.</span>
<span id="L1583">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L1584">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L1585">                                ! interior.</span>
<span id="L1586">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L1587">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L1588">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L1589">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L1590">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L1591">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L1592">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L1593">                                ! iterations is often this value or the next greater integer.</span>
<span id="L1594">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L1595">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L1596">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L1597">                                ! positions of the surfaces do not change</span>
<span id="L1598"></span>
<span id="L1599">! === module MOM_neutral_diffusion ===</span>
<span id="L1600">! This module implements neutral diffusion of tracers</span>
<span id="L1601">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L1602">                                ! If true, enables the neutral diffusion module.</span>
<span id="L1603"></span>
<span id="L1604">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1605">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1606">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1607">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1608">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1609">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1610">                                ! error rather than issue a WARNING.</span>
<span id="L1611"></span>
<span id="L1612">! === module MOM_sum_output ===</span>
<span id="L1613">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1614">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1615">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1616">                                ! dramatically.</span>
<span id="L1617">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1618">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1619">                                ! are written.</span>
<span id="L1620">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L1621">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1622">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1623">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1624">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1625">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1626">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1627">                                ! 10*MAXVEL^2.</span>
<span id="L1628">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L1629">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1630">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1631">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1632">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L1633">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1634">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1635">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1636">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L1637">                                ! The time unit in seconds a number of input fields</span>
<span id="L1638">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1639">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1640">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1641">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1642">                                ! file.</span>
<span id="L1643">ENERGYSAVEDAYS = 10.0           !   [days] default = 1.0</span>
<span id="L1644">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1645">                                ! other globally summed diagnostics.</span>
<span id="L1646">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L1647">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1648">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1649">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1650"></span>
<span id="L1651">! === module ocean_stochastics_init ===</span>
<span id="L1652">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1653">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1654">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1655">                                ! UFS model only.</span>
<span id="L1656">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1657">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1658">                                ! energy backscatter scheme.</span>
<span id="L1659">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1660">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1661">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1662">                                ! namelist in the UFS model only.</span>
<span id="L1663"></span>
<span id="L1664">! === module MOM_surface_forcing ===</span>
<span id="L1665">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L1666">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1667">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L1668">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1669">                                ! model.</span>
<span id="L1670">BUOY_CONFIG = &quot;data_override&quot;   ! default = &quot;zero&quot;</span>
<span id="L1671">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1672">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1673">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1674">WIND_CONFIG = &quot;data_override&quot;   ! default = &quot;zero&quot;</span>
<span id="L1675">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1676">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1677">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1678">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L1679">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1680">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1681">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1682">                                ! The latent heat of fusion.</span>
<span id="L1683">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1684">                                ! The latent heat of fusion.</span>
<span id="L1685">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1686">                                ! The background gustiness in the winds.</span>
<span id="L1687">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L1688">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L1689">                                ! velocity</span>
<span id="L1690">READ_GUST_2D = True             !   [Boolean] default = False</span>
<span id="L1691">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L1692">GUST_2D_FILE = &quot;forcing_monthly.nc&quot; !</span>
<span id="L1693">                                ! The file in which the wind gustiness is found in variable gustiness.</span>
<span id="L1694"></span>
<span id="L1695">! === module MOM_restart ===</span>
<span id="L1696">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L1697">                                ! If true, enables surface wave modules.</span>
<span id="L1698"></span>
<span id="L1699">! === module MOM_main (MOM_driver) ===</span>
<span id="L1700">DT_FORCING = 3600.0             !   [s] default = 3600.0</span>
<span id="L1701">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L1702">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L1703">DAYMAX = 180.0                  !   [days]</span>
<span id="L1704">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L1705">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L1706">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L1707">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L1708">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L1709">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L1710">RESTART_CONTROL = 0             ! default = 1</span>
<span id="L1711">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L1712">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L1713">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L1714">                                ! non-negative value.</span>
<span id="L1715">RESTINT = 3650.0                !   [days] default = 0.0</span>
<span id="L1716">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L1717">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L1718">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L1719">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L1720">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L1721">                                ! an elapsed CPU time.</span>
<span id="L1722"></span>
<span id="L1723">! === module MOM_write_cputime ===</span>
<span id="L1724">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L1725">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L1726">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L1727">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L1728">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L1729">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L1730">                                ! processors used.</span>
<span id="L1731">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L1732">                                ! The file into which CPU time is written.</span>
<span id="L1733"></span>
<span id="L1734">! === module MOM_file_parser ===</span>
<span id="L1735">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L1736">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L1737">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L1738">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L1739">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L1740">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L1741">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L1742">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L1743">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L1744">                                ! MOM_parameter_doc.short .</span>
</pre>
