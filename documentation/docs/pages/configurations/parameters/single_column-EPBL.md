---
search:
  exclude: true
---

# single_column-EPBL: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [single_column-EPBL](../mom6examples/single_column-EPBL.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

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
<span id="L37">USE_REGRIDDING = True           !   [Boolean] default = False</span>
<span id="L38">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L39">                                ! layered isopycnal algorithm.</span>
<span id="L40">REMAP_UV_USING_OLD_ALG = False  !   [Boolean] default = False</span>
<span id="L41">                                ! If true, uses the old remapping-via-a-delta-z method for remapping u and v. If</span>
<span id="L42">                                ! false, uses the new method that remaps between grids described by an old and</span>
<span id="L43">                                ! new thickness.</span>
<span id="L44">REMAP_AUXILIARY_VARS = False    !   [Boolean] default = False</span>
<span id="L45">                                ! If true, apply ALE remapping to all of the auxiliary 3-dimensional variables</span>
<span id="L46">                                ! that are needed to reproduce across restarts, similarly to what is already</span>
<span id="L47">                                ! being done with the primary state variables.  The default should be changed to</span>
<span id="L48">                                ! true.</span>
<span id="L49">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L50">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L51">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L52">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L53">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L54">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L55">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L56">                                ! edges of the grid cells.</span>
<span id="L57">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L58">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L59">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L60">                                ! points.</span>
<span id="L61">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L62">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L63">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L64">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L65">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L66">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L67">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L68">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L69">DT = 3600.0                     !   [s]</span>
<span id="L70">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L71">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L72">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L73">DT_THERM = 3600.0               !   [s] default = 3600.0</span>
<span id="L74">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L75">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L76">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L77">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L78">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L79">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L80">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L81">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L82">                                ! equal to DT_THERM.</span>
<span id="L83">DT_TRACER_ADVECT = 3600.0       !   [s] default = 3600.0</span>
<span id="L84">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L85">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L86">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L87">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L88">                                ! DT_THERM.</span>
<span id="L89">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L90">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L91">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L92">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L93">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L94">THICKNESSDIFFUSE = False        !   [Boolean] default = False</span>
<span id="L95">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L96">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L97">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L98">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L99">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L100">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L101">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L102">                                ! velocities).</span>
<span id="L103">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L104">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L105">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L106">                                ! indicates no averaging.</span>
<span id="L107">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L108">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L109">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L110">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L111">                                ! computed.</span>
<span id="L112">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L113">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L114">                                ! step, using the specified value at the end of the step.</span>
<span id="L115">FRAZIL = True                   !   [Boolean] default = False</span>
<span id="L116">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L117">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L118">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L119">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L120">                                ! If true, apply geothermal heating.</span>
<span id="L121">BOUND_SALINITY = False          !   [Boolean] default = False</span>
<span id="L122">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L123">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L124">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L125">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L126">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L127">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L128">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L129">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L130">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L131">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L132">                                ! definition of conservative temperature.</span>
<span id="L133">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L134">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L135">                                ! state calculations.</span>
<span id="L136">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L137">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L138">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L139">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L140">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L141">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L142">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L143">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L144">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L145">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L146">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L147">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L148">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L149">                                ! and odd numbers used for y-first.</span>
<span id="L150">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L151">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L152">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L153">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L154">                                ! first direction can not be found in the restart file.</span>
<span id="L155">CHECK_BAD_SURFACE_VALS = False  !   [Boolean] default = False</span>
<span id="L156">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L157">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L158">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L159">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L160">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L161">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L162">                                ! updated and more robust forms of the same expressions.</span>
<span id="L163">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
<span id="L164">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L165">IC_OUTPUT_FILE = &quot;MOM_IC&quot;       ! default = &quot;MOM_IC&quot;</span>
<span id="L166">                                ! The file into which to write the initial conditions.</span>
<span id="L167">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L168">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L169">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L170">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L171">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L172">                                ! The file into which to write the ocean geometry.</span>
<span id="L173">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L174">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L175">                                ! analysis and machine-learning inference.</span>
<span id="L176">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L177">                                ! If true, enables the ice shelf model.</span>
<span id="L178">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L179">                                ! If true, use the particles package.</span>
<span id="L180">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L181">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L182">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L183">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L184">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L185">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L186">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L187">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L188">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L189"></span>
<span id="L190">! === module MOM_domains ===</span>
<span id="L191">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L192">                                ! If true, the domain is zonally reentrant.</span>
<span id="L193">REENTRANT_Y = True              !   [Boolean] default = False</span>
<span id="L194">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L195">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L196">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L197">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L198">NIGLOBAL = 2                    !</span>
<span id="L199">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L200">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L201">NJGLOBAL = 2                    !</span>
<span id="L202">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L203">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L204">NIHALO = 2                      ! default = 4</span>
<span id="L205">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L206">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L207">NJHALO = 2                      ! default = 4</span>
<span id="L208">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L209">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L210"></span>
<span id="L211">! === module MOM_hor_index ===</span>
<span id="L212">! Sets the horizontal array index types.</span>
<span id="L213"></span>
<span id="L214">! === module MOM_grid ===</span>
<span id="L215">! Parameters providing information about the lateral grid.</span>
<span id="L216">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L217">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L218"></span>
<span id="L219">! === module MOM_fixed_initialization ===</span>
<span id="L220">INPUTDIR = &quot;INPUT/BATS&quot;         ! default = &quot;.&quot;</span>
<span id="L221">                                ! The directory in which input files are found.</span>
<span id="L222"></span>
<span id="L223">! === module MOM_grid_init ===</span>
<span id="L224">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L225">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L226">                                ! grid.  Current options are:</span>
<span id="L227">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L228">                                !              file set by GRID_FILE.</span>
<span id="L229">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L230">                                !     spherical - use a simple spherical grid.</span>
<span id="L231">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L232">AXIS_UNITS = &quot;degrees&quot;          ! default = &quot;degrees&quot;</span>
<span id="L233">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L234">                                !     degrees - degrees of latitude and longitude</span>
<span id="L235">                                !     m or meter(s) - meters</span>
<span id="L236">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L237">SOUTHLAT = 30.0                 !   [degrees]</span>
<span id="L238">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L239">                                ! y-axis.</span>
<span id="L240">LENLAT = 1.0                    !   [degrees]</span>
<span id="L241">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L242">WESTLON = 0.0                   !   [degrees] default = 0.0</span>
<span id="L243">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L244">                                ! x-axis.</span>
<span id="L245">LENLON = 1.0                    !   [degrees]</span>
<span id="L246">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L247">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L248">                                ! The radius of the Earth.</span>
<span id="L249">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L250">                                ! This specifies how bathymetry is specified:</span>
<span id="L251">                                !     file - read bathymetric information from the file</span>
<span id="L252">                                !       specified by (TOPO_FILE).</span>
<span id="L253">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L254">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L255">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L256">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L257">                                !       wall at the southern face.</span>
<span id="L258">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L259">                                !       profile in the meridional direction.</span>
<span id="L260">                                !     bbuilder - build topography from list of functions.</span>
<span id="L261">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L262">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L263">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L264">                                !       DOME sill-overflow test case.</span>
<span id="L265">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L266">                                !       ISOMIP test case.</span>
<span id="L267">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L268">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L269">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L270">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L271">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L272">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L273">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L274">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L275">                                !     USER - call a user modified routine.</span>
<span id="L276">MINIMUM_DEPTH = 0.5             !   [m] default = 0.0</span>
<span id="L277">                                ! The minimum depth of the ocean.</span>
<span id="L278">MAXIMUM_DEPTH = 6000.0          !   [m]</span>
<span id="L279">                                ! The maximum depth of the ocean.</span>
<span id="L280"></span>
<span id="L281">! === module MOM_open_boundary ===</span>
<span id="L282">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L283">! if any.</span>
<span id="L284">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L285">                                ! The number of open boundary segments.</span>
<span id="L286">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L287">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L288">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L289">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L290">                                ! A parameter that determines which set of channels are</span>
<span id="L291">                                ! restricted to specific  widths.  Options are:</span>
<span id="L292">                                !     none - All channels have the grid width.</span>
<span id="L293">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L294">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L295">                                !     list - Read the channel locations and widths from a</span>
<span id="L296">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L297">                                !       test case.</span>
<span id="L298">                                !     file - Read open face widths everywhere from a</span>
<span id="L299">                                !       NetCDF file on the model grid.</span>
<span id="L300">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L301">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L302">ROTATION = &quot;betaplane&quot;          ! default = &quot;2omegasinlat&quot;</span>
<span id="L303">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L304">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L305">                                !       times the sine of latitude.</span>
<span id="L306">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L307">                                !     USER - call a user modified routine.</span>
<span id="L308">F_0 = 7.59943E-05               !   [s-1] default = 0.0</span>
<span id="L309">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L310">BETA = 0.0                      !   [m-1 s-1] default = 0.0</span>
<span id="L311">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L312">BETA_LAT_REF = 0.0              !   [degrees] default = 0.0</span>
<span id="L313">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L314">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L315">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L316">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L317">                                ! arise at the tripolar fold.</span>
<span id="L318"></span>
<span id="L319">! === module MOM_verticalGrid ===</span>
<span id="L320">! Parameters providing information about the vertical grid.</span>
<span id="L321">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L322">                                ! The gravitational acceleration of the Earth.</span>
<span id="L323">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L324">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L325">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L326">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L327">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L328">                                ! If true, make the Boussinesq approximation.</span>
<span id="L329">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L330">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L331">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L332">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L333">NK = 75                         !   [nondim]</span>
<span id="L334">                                ! The number of model layers.</span>
<span id="L335">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L336">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L337">                                ! production is set to 0.</span>
<span id="L338"></span>
<span id="L339">! === module MOM_tracer_registry ===</span>
<span id="L340"></span>
<span id="L341">! === module MOM_EOS ===</span>
<span id="L342">EQN_OF_STATE = &quot;WRIGHT&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L343">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L344">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L345">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L346">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L347">USE_WRIGHT_2ND_DERIV_BUG = False !   [Boolean] default = False</span>
<span id="L348">                                ! If true, use a bug in the calculation of the second derivatives of density</span>
<span id="L349">                                ! with temperature and with temperature and pressure that causes some terms to</span>
<span id="L350">                                ! be only 2/3 of what they should be.</span>
<span id="L351">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L352">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L353">                                ! density.</span>
<span id="L354">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L355">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L356">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L357">                                ! &quot;TEOS10&quot;</span>
<span id="L358">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L359">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L360">                                ! P=0.</span>
<span id="L361">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L362">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L363">                                ! temperature with salinity.</span>
<span id="L364">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L365">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L366">                                ! temperature with pressure.</span>
<span id="L367">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L368">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L369">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L370">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L371">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L372">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L373">                                ! applied.</span>
<span id="L374"></span>
<span id="L375">! === module MOM_restart ===</span>
<span id="L376">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L377">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L378">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L379">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L380">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L381">                                ! The name-root of the restart file.</span>
<span id="L382">MAX_FIELDS = 100                ! default = 100</span>
<span id="L383">                                ! The maximum number of restart fields that can be used.</span>
<span id="L384">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L385">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L386">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L387">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L388">                                ! checksums will not match and cause crash.</span>
<span id="L389">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L390">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L391">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L392">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L393">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L394">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L395">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L396"></span>
<span id="L397">! === module MOM_tracer_flow_control ===</span>
<span id="L398">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L399">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L400">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L401">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L402">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L403">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L404">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L405">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L406">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L407">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L408">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L409">                                ! If true, use the MARBL tracer package.</span>
<span id="L410">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L411">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L412">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L413">                                ! If true, use the file dyes tracer package.</span>
<span id="L414">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L415">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L416">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L417">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L418">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L419">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L420">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L421">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L422">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L423">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L424">                                ! MOM_generic_tracer packages.</span>
<span id="L425">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L426">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L427">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L428">                                ! If true, use the boundary impulse tracer.</span>
<span id="L429">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L430">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L431">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L432">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L433"></span>
<span id="L434">! === module MOM_coord_initialization ===</span>
<span id="L435">COORD_CONFIG = &quot;none&quot;           ! default = &quot;none&quot;</span>
<span id="L436">                                ! This specifies how layers are to be defined:</span>
<span id="L437">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L438">                                !     file - read coordinate information from the file</span>
<span id="L439">                                !       specified by (COORD_FILE).</span>
<span id="L440">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L441">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L442">                                !     linear - linear based on interfaces not layers</span>
<span id="L443">                                !     layer_ref - linear based on layer densities</span>
<span id="L444">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L445">                                !     ts_range - use range of temperature and salinity</span>
<span id="L446">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L447">                                !       and GINT calculate internal densities.</span>
<span id="L448">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L449">                                !       density and GINT calculate internal densities.</span>
<span id="L450">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L451">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L452">                                !     USER - call a user modified routine.</span>
<span id="L453">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L454">                                ! The reduced gravity at the free surface.</span>
<span id="L455">LIGHTEST_DENSITY = 1035.0       !   [kg m-3] default = 1035.0</span>
<span id="L456">                                ! The reference potential density used for layer 1.</span>
<span id="L457">REGRIDDING_COORDINATE_MODE = &quot;Z*&quot; ! default = &quot;LAYER&quot;</span>
<span id="L458">                                ! Coordinate mode for vertical regridding. Choose among the following</span>
<span id="L459">                                ! possibilities:  LAYER - Isopycnal or stacked shallow water layers</span>
<span id="L460">                                !  ZSTAR, Z* - stretched geopotential z*</span>
<span id="L461">                                !  SIGMA_SHELF_ZSTAR - stretched geopotential z* ignoring shelf</span>
<span id="L462">                                !  SIGMA - terrain following coordinates</span>
<span id="L463">                                !  RHO   - continuous isopycnal</span>
<span id="L464">                                !  HYCOM1 - HyCOM-like hybrid coordinate</span>
<span id="L465">                                !  HYBGEN - Hybrid coordinate from the Hycom hybgen code</span>
<span id="L466">                                !  ADAPTIVE - optimize for smooth neutral density surfaces</span>
<span id="L467">REGRIDDING_COORDINATE_UNITS = &quot;m&quot; ! default = &quot;m&quot;</span>
<span id="L468">                                ! Units of the regridding coordinate.</span>
<span id="L469">ALE_COORDINATE_CONFIG = &quot;FILE:./INPUT/vgrid_cm4.nc,dz&quot; ! default = &quot;UNIFORM&quot;</span>
<span id="L470">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L471">                                !  PARAM       - use the vector-parameter ALE_RESOLUTION</span>
<span id="L472">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L473">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L474">                                !                the filename and variable name, separated</span>
<span id="L475">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L476">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L477">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L478">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L479">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L480">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L481">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L482">                                !                the filename and two variable names, separated</span>
<span id="L483">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L484">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L485">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L486">                                !                the filename and two 3D variable names, separated</span>
<span id="L487">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L488">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L489">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L490">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L491">                                !                the filename and three variable names, separated</span>
<span id="L492">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L493">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L494">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L495">                                !                Map typically contains integer values, but it can</span>
<span id="L496">                                !                contain real values, I+w, which imply using</span>
<span id="L497">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L498">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L499">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L500">!ALE_RESOLUTION = 4*2.0, 2*2.01, 2*2.02, 2.05, 2.07, 2.09, 2.13, 2.18, 2.24, 2.3, 2.4, 2.5, 2.62, 2.78, 2.95, 3.17, 3.42, 3.71, 4.07, 4.48, 4.97, 5.55, 6.23, 7.04, 7.99, 9.11, 10.43, 11.98, 13.8, 15.94, 18.42, 21.32, 24.66, 28.51, 32.91, 37.92, 43.56, 49.87, 56.88, 64.55, 72.91, 81.87, 91.4, 101.39, 111.73, 122.29, 132.93, 143.47, 153.78, 163.7, 173.07, 181.78, 189.76, 196.89, 203.17, 208.58, 213.14, 216.87, 219.87, 222.19, 223.94, 225.18, 226.04, 226.59, 226.9, 227.07, 227.14, 2*227.16, 227.17 !   [m]</span>
<span id="L501">                                ! The distribution of vertical resolution for the target</span>
<span id="L502">                                ! grid used for Eulerian-like coordinates. For example,</span>
<span id="L503">                                ! in z-coordinate mode, the parameter is a list of level</span>
<span id="L504">                                ! thicknesses (in m). In sigma-coordinate mode, the list</span>
<span id="L505">                                ! is of non-dimensional fractions of the water column.</span>
<span id="L506">MIN_THICKNESS = 0.001           !   [m] default = 0.001</span>
<span id="L507">                                ! When regridding, this is the minimum layer thickness allowed.</span>
<span id="L508">REMAPPING_SCHEME = &quot;PLM&quot;        ! default = &quot;PLM&quot;</span>
<span id="L509">                                ! This sets the reconstruction scheme used for vertical remapping for all</span>
<span id="L510">                                ! variables. It can be one of the following schemes:</span>
<span id="L511">                                ! PCM         (1st-order accurate)</span>
<span id="L512">                                ! PLM         (2nd-order accurate)</span>
<span id="L513">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L514">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L515">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L516">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L517">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L518">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L519">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L520">VELOCITY_REMAPPING_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L521">                                ! This sets the reconstruction scheme used for vertical remapping of velocities.</span>
<span id="L522">                                ! By default it is the same as REMAPPING_SCHEME. It can be one of the following</span>
<span id="L523">                                ! schemes:</span>
<span id="L524">                                ! PCM         (1st-order accurate)</span>
<span id="L525">                                ! PLM         (2nd-order accurate)</span>
<span id="L526">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L527">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L528">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L529">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L530">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L531">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L532">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L533">FATAL_CHECK_RECONSTRUCTIONS = False !   [Boolean] default = False</span>
<span id="L534">                                ! If true, cell-by-cell reconstructions are checked for consistency and if</span>
<span id="L535">                                ! non-monotonicity or an inconsistency is detected then a FATAL error is issued.</span>
<span id="L536">FATAL_CHECK_REMAPPING = False   !   [Boolean] default = False</span>
<span id="L537">                                ! If true, the results of remapping are checked for conservation and new extrema</span>
<span id="L538">                                ! and if an inconsistency is detected then a FATAL error is issued.</span>
<span id="L539">REMAP_BOUND_INTERMEDIATE_VALUES = False !   [Boolean] default = False</span>
<span id="L540">                                ! If true, the values on the intermediate grid used for remapping are forced to</span>
<span id="L541">                                ! be bounded, which might not be the case due to round off.</span>
<span id="L542">REMAP_BOUNDARY_EXTRAP = False   !   [Boolean] default = False</span>
<span id="L543">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L544">                                ! of piecewise constant</span>
<span id="L545">INIT_BOUNDARY_EXTRAP = False    !   [Boolean] default = False</span>
<span id="L546">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L547">                                ! of piecewise constant during initialization.Defaults to REMAP_BOUNDARY_EXTRAP.</span>
<span id="L548">REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L549">                                ! This selects the remapping algorithm used in OM4 that does not use the full</span>
<span id="L550">                                ! reconstruction for the top- and lower-most sub-layers, but instead assumes</span>
<span id="L551">                                ! they are always vanished (untrue) and so just uses their edge values. We</span>
<span id="L552">                                ! recommend setting this option to false.</span>
<span id="L553">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L554">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L555">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L556">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L557">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L558">PARTIAL_CELL_VELOCITY_REMAP = False !   [Boolean] default = False</span>
<span id="L559">                                ! If true, use partial cell thicknesses at velocity points that are masked out</span>
<span id="L560">                                ! where they extend below the shallower of the neighboring bathymetry for</span>
<span id="L561">                                ! remapping velocity.</span>
<span id="L562">REMAP_AFTER_INITIALIZATION = True !   [Boolean] default = True</span>
<span id="L563">                                ! If true, applies regridding and remapping immediately after initialization so</span>
<span id="L564">                                ! that the state is ALE consistent. This is a legacy step and should not be</span>
<span id="L565">                                ! needed if the initialization is consistent with the coordinate mode.</span>
<span id="L566">REGRID_TIME_SCALE = 0.0         !   [s] default = 0.0</span>
<span id="L567">                                ! The time-scale used in blending between the current (old) grid and the target</span>
<span id="L568">                                ! (new) grid. A short time-scale favors the target grid (0. or anything less</span>
<span id="L569">                                ! than DT_THERM) has no memory of the old grid. A very long time-scale makes the</span>
<span id="L570">                                ! model more Lagrangian.</span>
<span id="L571">REGRID_FILTER_SHALLOW_DEPTH = 0.0 !   [m] default = 0.0</span>
<span id="L572">                                ! The depth above which no time-filtering is applied. Above this depth final</span>
<span id="L573">                                ! grid exactly matches the target (new) grid.</span>
<span id="L574">REGRID_FILTER_DEEP_DEPTH = 0.0  !   [m] default = 0.0</span>
<span id="L575">                                ! The depth below which full time-filtering is applied with time-scale</span>
<span id="L576">                                ! REGRID_TIME_SCALE. Between depths REGRID_FILTER_SHALLOW_DEPTH and</span>
<span id="L577">                                ! REGRID_FILTER_SHALLOW_DEPTH the filter weights adopt a cubic profile.</span>
<span id="L578">REMAP_VEL_MASK_BBL_THICK = -0.001 !   [m] default = -0.001</span>
<span id="L579">                                ! A thickness of a bottom boundary layer below which velocities in thin layers</span>
<span id="L580">                                ! are zeroed out after remapping, following practice with Hybgen remapping, or a</span>
<span id="L581">                                ! negative value to avoid such filtering altogether.</span>
<span id="L582">REMAP_VEL_CONSERVE_KE = False   !   [Boolean] default = False</span>
<span id="L583">                                ! If true, a correction is applied to the baroclinic component of velocity after</span>
<span id="L584">                                ! remapping so that total KE is conserved. KE may not be conserved when</span>
<span id="L585">                                ! (CS%BBL_h_vel_mask &gt; 0.0) .and. (CS%h_vel_mask &gt; 0.0)</span>
<span id="L586"></span>
<span id="L587">! === module MOM_state_initialization ===</span>
<span id="L588">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L589">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L590">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L591">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L592">INIT_LAYERS_FROM_Z_FILE = True  !   [Boolean] default = False</span>
<span id="L593">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L594">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L595"></span>
<span id="L596">! === module MOM_initialize_layers_from_Z ===</span>
<span id="L597">TEMP_SALT_Z_INIT_FILE = &quot;WOA_column.nc&quot; ! default = &quot;temp_salt_z.nc&quot;</span>
<span id="L598">                                ! The name of the z-space input file used to initialize temperatures (T) and</span>
<span id="L599">                                ! salinities (S). If T and S are not in the same file, TEMP_Z_INIT_FILE and</span>
<span id="L600">                                ! SALT_Z_INIT_FILE must be set.</span>
<span id="L601">TEMP_Z_INIT_FILE = &quot;WOA_column.nc&quot; ! default = &quot;WOA_column.nc&quot;</span>
<span id="L602">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L603">SALT_Z_INIT_FILE = &quot;WOA_column.nc&quot; ! default = &quot;WOA_column.nc&quot;</span>
<span id="L604">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L605">Z_INIT_FILE_PTEMP_VAR = &quot;PTEMP&quot; ! default = &quot;ptemp&quot;</span>
<span id="L606">                                ! The name of the potential temperature variable in TEMP_Z_INIT_FILE.</span>
<span id="L607">Z_INIT_FILE_SALT_VAR = &quot;SALT&quot;   ! default = &quot;salt&quot;</span>
<span id="L608">                                ! The name of the salinity variable in SALT_Z_INIT_FILE.</span>
<span id="L609">Z_INIT_HOMOGENIZE = True        !   [Boolean] default = False</span>
<span id="L610">                                ! If True, then horizontally homogenize the interpolated initial conditions.</span>
<span id="L611">Z_INIT_ALE_REMAPPING = True     !   [Boolean] default = False</span>
<span id="L612">                                ! If True, then remap straight to model coordinate from file.</span>
<span id="L613">Z_INIT_REMAPPING_SCHEME = &quot;PPM_IH4&quot; ! default = &quot;PPM_IH4&quot;</span>
<span id="L614">                                ! The remapping scheme to use if using Z_INIT_ALE_REMAPPING is True.</span>
<span id="L615">Z_INIT_REMAP_GENERAL = False    !   [Boolean] default = False</span>
<span id="L616">                                ! If false, only initializes to z* coordinates. If true, allows initialization</span>
<span id="L617">                                ! directly to general coordinates.</span>
<span id="L618">Z_INIT_REMAP_FULL_COLUMN = False !   [Boolean] default = False</span>
<span id="L619">                                ! If false, only reconstructs profiles for valid data points. If true, inserts</span>
<span id="L620">                                ! vanished layers below the valid data.</span>
<span id="L621">Z_INIT_REMAP_OLD_ALG = False    !   [Boolean] default = False</span>
<span id="L622">                                ! If false, uses the preferred remapping algorithm for initialization. If true,</span>
<span id="L623">                                ! use an older, less robust algorithm for remapping.</span>
<span id="L624">TEMP_SALT_INIT_VERTICAL_REMAP_ONLY = False !   [Boolean] default = False</span>
<span id="L625">                                ! If true, initial conditions are on the model horizontal grid. Extrapolation</span>
<span id="L626">                                ! over missing ocean values is done using an ICE-9 procedure with vertical ALE</span>
<span id="L627">                                ! remapping .</span>
<span id="L628">Z_INIT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L629">                                ! If true, use the OM4 remapping-via-subcells algorithm for initialization. See</span>
<span id="L630">                                ! REMAPPING_USE_OM4_SUBCELLS for more details. We recommend setting this option</span>
<span id="L631">                                ! to false.</span>
<span id="L632">HOR_REGRID_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L633">                                ! The vintage of the order of arithmetic for horizontal regridding.  Dates</span>
<span id="L634">                                ! before 20190101 give the same answers as the code did in late 2018, while</span>
<span id="L635">                                ! later versions add parentheses for rotational symmetry.  Dates after 20230101</span>
<span id="L636">                                ! use reproducing sums for global averages.</span>
<span id="L637">LAND_FILL_TEMP = 0.0            !   [degC] default = 0.0</span>
<span id="L638">                                ! A value to use to fill in ocean temperatures on land points.</span>
<span id="L639">LAND_FILL_SALIN = 35.0          !   [ppt] default = 35.0</span>
<span id="L640">                                ! A value to use to fill in ocean salinities on land points.</span>
<span id="L641">HORIZ_INTERP_TOL_TEMP = 0.001   !   [degC] default = 0.001</span>
<span id="L642">                                ! The tolerance in temperature changes between iterations when interpolating</span>
<span id="L643">                                ! from an input dataset using horiz_interp_and_extrap_tracer.  This routine</span>
<span id="L644">                                ! converges slowly, so an overly small tolerance can get expensive.</span>
<span id="L645">HORIZ_INTERP_TOL_SALIN = 0.001  !   [ppt] default = 0.001</span>
<span id="L646">                                ! The tolerance in salinity changes between iterations when interpolating from</span>
<span id="L647">                                ! an input dataset using horiz_interp_and_extrap_tracer.  This routine converges</span>
<span id="L648">                                ! slowly, so an overly small tolerance can get expensive.</span>
<span id="L649">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L650">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L651">                                ! surface pressure is applied.</span>
<span id="L652">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L653">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L654">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L655">                                ! read from file.</span>
<span id="L656">REGRID_ACCELERATE_INIT = False  !   [Boolean] default = False</span>
<span id="L657">                                ! If true, runs REGRID_ACCELERATE_ITERATIONS iterations of the regridding</span>
<span id="L658">                                ! algorithm to push the initial grid to be consistent with the initial</span>
<span id="L659">                                ! condition. Useful only for state-based and iterative coordinates.</span>
<span id="L660">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L661">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L662">                                ! run:</span>
<span id="L663">                                !     file - read velocities from the file specified</span>
<span id="L664">                                !       by (VELOCITY_FILE).</span>
<span id="L665">                                !     zero - the fluid is initially at rest.</span>
<span id="L666">                                !     uniform - the flow is uniform (determined by</span>
<span id="L667">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L668">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L669">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L670">                                !     USER - call a user modified routine.</span>
<span id="L671">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L672">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L673">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L674">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L675">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L676"></span>
<span id="L677">! === module MOM_diag_mediator ===</span>
<span id="L678">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L679">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L680">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L681">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L682">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L683">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L684">                                ! false.</span>
<span id="L685">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L686">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L687">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L688">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L689">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L690">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L691">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L692">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L693">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L694">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L695">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L696">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L697">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L698">                                ! be included in a diag_table.</span>
<span id="L699">DIAG_COORD_DEF_Z = &quot;WOA09&quot;      ! default = &quot;WOA09&quot;</span>
<span id="L700">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L701">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L702">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L703">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L704">                                !                the filename and variable name, separated</span>
<span id="L705">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L706">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L707">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L708">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L709">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L710">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L711">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L712">                                !                the filename and two variable names, separated</span>
<span id="L713">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L714">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L715">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L716">                                !                the filename and two 3D variable names, separated</span>
<span id="L717">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L718">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L719">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L720">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L721">                                !                the filename and three variable names, separated</span>
<span id="L722">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L723">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L724">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L725">                                !                Map typically contains integer values, but it can</span>
<span id="L726">                                !                contain real values, I+w, which imply using</span>
<span id="L727">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L728">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L729">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L730"></span>
<span id="L731">! === module MOM_MEKE ===</span>
<span id="L732">USE_MEKE = False                !   [Boolean] default = False</span>
<span id="L733">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L734">                                ! kinetic energy budget.</span>
<span id="L735"></span>
<span id="L736">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L737">USE_VARIABLE_MIXING = False     !   [Boolean] default = False</span>
<span id="L738">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L739">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L740">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L741">                                ! file.</span>
<span id="L742">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L743">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L744">                                ! thickness diffusivity.</span>
<span id="L745">RESOLN_SCALED_KH = False        !   [Boolean] default = False</span>
<span id="L746">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L747">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L748">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L749">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L750">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L751">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L752">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L753">RESOLN_SCALED_KHTH = False      !   [Boolean] default = False</span>
<span id="L754">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L755">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L756">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L757">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L758">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L759">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L760">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L761">                                ! wave for calculating the resolution fn.</span>
<span id="L762">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L763">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L764">                                ! structure.</span>
<span id="L765">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L766">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L767">                                ! that BS_EBT_power=0</span>
<span id="L768">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L769">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L770">                                ! thickness diffusivity.</span>
<span id="L771">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L772">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L773">                                ! of thickness diffusivity.</span>
<span id="L774">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L775">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L776">                                ! tracer diffusivity.</span>
<span id="L777">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L778">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L779">                                ! of tracer diffusivity.</span>
<span id="L780">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L781">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L782">                                ! diffusivity in the GL90 scheme.</span>
<span id="L783">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L784">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L785">                                ! diffusivity in the GL90 scheme.</span>
<span id="L786">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L787">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L788">                                ! diffusivity</span>
<span id="L789">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L790">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L791">                                ! diffusivity</span>
<span id="L792">USE_STORED_SLOPES = False       !   [Boolean] default = False</span>
<span id="L793">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L794">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L795">                                ! should be necessary.</span>
<span id="L796">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L797">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L798">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L799">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L800">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L801">                                ! code.</span>
<span id="L802">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L803">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L804">                                ! &amp; S into thin layers.</span>
<span id="L805">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L806">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L807"></span>
<span id="L808">! === module MOM_set_visc ===</span>
<span id="L809">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L810">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L811">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L812">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L813">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L814">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L815">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L816">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L817">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L818">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L819">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L820">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L821">                                ! layer is HBBL.</span>
<span id="L822">CHANNEL_DRAG = False            !   [Boolean] default = False</span>
<span id="L823">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L824">                                ! fraction of the bottom it overlies.</span>
<span id="L825">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L826">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L827">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L828">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L829">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L830">                                ! thickness for viscosity.</span>
<span id="L831">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L832">                                ! The rotation rate of the earth.</span>
<span id="L833">HBBL = 10.0                     !   [m]</span>
<span id="L834">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L835">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L836">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L837">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L838">CDRAG = 0.0                     !   [nondim] default = 0.003</span>
<span id="L839">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L840">                                ! the bottom stress. CDRAG is only used if BOTTOMDRAGLAW is defined.</span>
<span id="L841">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L842">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L843">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L844">                                ! and LINEAR_DRAG is false.</span>
<span id="L845">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L846">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L847">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L848">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L849">                                ! defined.</span>
<span id="L850">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L851">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L852">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L853">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L854">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L855">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L856">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L857">                                ! near-bottom viscosity.</span>
<span id="L858">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L859">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L860">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L861">                                ! viscosity.</span>
<span id="L862">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L863">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L864">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L865">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L866">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L867">                                ! m2 s-1, may be used.</span>
<span id="L868">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L869">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L870">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L871">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L872">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L873">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L874">                                ! the bottom layer feels the intended drag.</span>
<span id="L875"></span>
<span id="L876">! === module MOM_thickness_diffuse ===</span>
<span id="L877">KHTH = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L878">                                ! The background horizontal thickness diffusivity.</span>
<span id="L879">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L880">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L881">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L882">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L883">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L884">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L885">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L886">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L887">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L888">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L889">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L890">                                ! models.</span>
<span id="L891">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L892">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L893">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L894">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L895">                                ! are scaled back proportionately.</span>
<span id="L896">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L897">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L898">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L899">                                ! the layer density structure).</span>
<span id="L900">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L901">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L902">                                ! horizontally smooth jagged layers.</span>
<span id="L903">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L904">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L905">                                ! scaled away.</span>
<span id="L906">KHTH_USE_FGNV_STREAMFUNCTION = False !   [Boolean] default = False</span>
<span id="L907">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L908">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L909">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L910">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L911">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L912">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L913">                                ! streamfunction for the GM source term.</span>
<span id="L914">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L915">                                ! If true, uses the GM coefficient formulation from the GEOMETRIC framework</span>
<span id="L916">                                ! (Marshall et al., 2012).</span>
<span id="L917">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L918">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L919">                                ! McWilliams parameterization.</span>
<span id="L920">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L921">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L922">                                ! sign, for legacy reproducibility.</span>
<span id="L923">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L924">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L925">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L926">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L927"></span>
<span id="L928">! === module MOM_dynamics_unsplit ===</span>
<span id="L929">UNSPLIT_DT_VISC_BUG = False     !   [Boolean] default = False</span>
<span id="L930">                                ! If false, use the correct timestep in the viscous terms applied in the first</span>
<span id="L931">                                ! predictor step with the unsplit time stepping scheme, and in the calculation</span>
<span id="L932">                                ! of the turbulent mixed layer properties for viscosity with unsplit or</span>
<span id="L933">                                ! unsplit_RK2.  If true, an older incorrect value is used.</span>
<span id="L934">TIDES = False                   !   [Boolean] default = False</span>
<span id="L935">                                ! If true, apply tidal momentum forcing.</span>
<span id="L936">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L937">                                ! If true, calculate self-attraction and loading.</span>
<span id="L938"></span>
<span id="L939">! === module MOM_continuity_PPM ===</span>
<span id="L940">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L941">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L942">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L943">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L944">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L945">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L946">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L947">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L948">                                ! of accuracy of the dynamic core.</span>
<span id="L949">UPWIND_1ST_CONTINUITY = True    !   [Boolean] default = False</span>
<span id="L950">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L951">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L952">                                ! mode where its minimal stencil is useful.</span>
<span id="L953">ETA_TOLERANCE = 1.0E-06         !   [m] default = 3.75E-09</span>
<span id="L954">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L955">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L956">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L957">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L958">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L959">VELOCITY_TOLERANCE = 3.0E+08    !   [m s-1] default = 3.0E+08</span>
<span id="L960">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L961">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L962">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L963">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L964">                                ! 0.5.</span>
<span id="L965">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L966">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L967">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L968">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L969">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L970">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L971">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L972">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L973">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L974">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L975">                                ! viscous columns.</span>
<span id="L976">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L977">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L978">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L979"></span>
<span id="L980">! === module MOM_CoriolisAdv ===</span>
<span id="L981">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L982">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L983">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L984">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L985">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L986">CORIOLIS_EN_DIS = True          !   [Boolean] default = False</span>
<span id="L987">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L988">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L989">                                ! used.</span>
<span id="L990">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L991">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L992">                                ! values are:</span>
<span id="L993">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L994">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L995">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L996">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L997">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L998">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L999">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1000">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1001">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1002">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1003">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1004">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1005">                                ! option is always effectively false with CORIOLIS_EN_DIS defined and</span>
<span id="L1006">                                ! CORIOLIS_SCHEME set to SADOURNY75_ENERGY.</span>
<span id="L1007">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1008">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1009">                                ! energy gradient. Valid values are:</span>
<span id="L1010">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1011">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1012">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1013">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1014">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1015"></span>
<span id="L1016">! === module MOM_PressureForce ===</span>
<span id="L1017">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1018">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1019">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1020">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1021">                                ! al., O. Mod. (2008).</span>
<span id="L1022"></span>
<span id="L1023">! === module MOM_PressureForce_FV ===</span>
<span id="L1024">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L1025">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1026">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1027">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1028">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1029">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1030">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1031">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1032">                                ! Boussinesq mode.</span>
<span id="L1033">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1034">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1035">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1036">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1037">                                ! pressure.</span>
<span id="L1038">MASS_WEIGHT_IN_PRESSURE_GRADIENT = False !   [Boolean] default = False</span>
<span id="L1039">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1040">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1041">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = False !   [Boolean] default = False</span>
<span id="L1042">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1043">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1044">                                ! pressure gradient calculations.</span>
<span id="L1045">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1046">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1047">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1048">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1049">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1050">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1051">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1052">                                ! pressure correction.</span>
<span id="L1053">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1054">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1055">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1056">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1057">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1058">                                ! inaccurate way. This is not recommended.</span>
<span id="L1059">RECONSTRUCT_FOR_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1060">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1061">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1062">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1063">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1064">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1065">                                ! pressure gradient calculation.</span>
<span id="L1066">                                !  0: PCM or no reconstruction.</span>
<span id="L1067">                                !  1: PLM reconstruction.</span>
<span id="L1068">                                !  2: PPM reconstruction.</span>
<span id="L1069">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1070">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1071">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1072">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1073">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1074">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1075"></span>
<span id="L1076">! === module MOM_Zanna_Bolton ===</span>
<span id="L1077">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1078">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1079">                                ! mesoscale eddies.</span>
<span id="L1080"></span>
<span id="L1081">! === module MOM_hor_visc ===</span>
<span id="L1082">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1083">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1084">                                ! Leith)</span>
<span id="L1085">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1086">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1087">                                ! currently only works with split mode.</span>
<span id="L1088">LAPLACIAN = False               !   [Boolean] default = False</span>
<span id="L1089">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1090">BIHARMONIC = False              !   [Boolean] default = True</span>
<span id="L1091">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1092">                                ! LAPLACIAN.</span>
<span id="L1093">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1094">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1095">                                ! harmonic backscatter.</span>
<span id="L1096">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1097">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1098">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1099">                                ! outside of the domain.</span>
<span id="L1100">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1101">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1102">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1103">                                ! recommended.</span>
<span id="L1104"></span>
<span id="L1105">! === module MOM_vert_friction ===</span>
<span id="L1106">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1107">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1108">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1109">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1110">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1111">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1112">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1113">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1114">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1115">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1116">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1117">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1118">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1119">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1120">                                ! of the ocean in a column.</span>
<span id="L1121">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1122">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1123">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1124">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1125">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1126">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1127">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1128">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1129">HARMONIC_VISC = True            !   [Boolean] default = False</span>
<span id="L1130">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1131">                                ! viscosity.</span>
<span id="L1132">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1133">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1134">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1135">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1136">HMIX_FIXED = 0.01               !   [m]</span>
<span id="L1137">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1138">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1139">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1140">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1141">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1142">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1143">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1144">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1145">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1146">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1147">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1148">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1149">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1150">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1151">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1152">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1153">                                ! default is CFL_TRUNCATE.</span>
<span id="L1154">CFL_TRUNCATE_RAMP_TIME = 0.0    !   [s] default = 0.0</span>
<span id="L1155">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1156">                                ! the run.</span>
<span id="L1157">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1158">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1159">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1160">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1161">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1162">VEL_UNDERFLOW = 1.0E-30         !   [m s-1] default = 0.0</span>
<span id="L1163">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1164">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1165">                                ! divided by the age of the universe.</span>
<span id="L1166"></span>
<span id="L1167">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1168">MIXEDLAYER_RESTRAT = False      !   [Boolean] default = False</span>
<span id="L1169">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1170">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1171">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1172"></span>
<span id="L1173">! === module MOM_diagnostics ===</span>
<span id="L1174">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1175">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1176">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1177">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1178">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1179">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1180">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1181">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1182">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1183">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1184">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L1185">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1186">                                ! starting point for iterations.</span>
<span id="L1187">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1188">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1189">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1190">                                ! this option to false.</span>
<span id="L1191"></span>
<span id="L1192">! === module MOM_diabatic_driver ===</span>
<span id="L1193">! The following parameters are used for diabatic processes.</span>
<span id="L1194">USE_LEGACY_DIABATIC_DRIVER = True !   [Boolean] default = True</span>
<span id="L1195">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1196">                                ! and is needed to avoid change in answers.</span>
<span id="L1197">ENERGETICS_SFC_PBL = True       !   [Boolean] default = False</span>
<span id="L1198">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1199">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1200">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1201">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1202">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1203">PRANDTL_EPBL = 1.0              !   [nondim] default = 1.0</span>
<span id="L1204">                                ! The Prandtl number used by ePBL to convert vertical diffusivities into</span>
<span id="L1205">                                ! viscosities.</span>
<span id="L1206">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1207">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1208">                                ! internal tide energy density.</span>
<span id="L1209">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1210">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1211">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1212">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1213">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1214">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1215">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1216">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1217">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1218">                                ! updated state.</span>
<span id="L1219">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1220">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1221">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1222">MIX_BOUNDARY_TRACER_ALE = False !   [Boolean] default = False</span>
<span id="L1223">                                ! If true and in ALE mode, mix the passive tracers in massless layers at the</span>
<span id="L1224">                                ! bottom into the interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1225">KD_MIN_TR = 2.0E-06             !   [m2 s-1] default = 2.0E-06</span>
<span id="L1226">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1227">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1228">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1229">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1230">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1231">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1232">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1233">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1234">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1235">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1236">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1237">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1238">                                ! scale.</span>
<span id="L1239">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1240">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1241">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1242">                                ! through the column.</span>
<span id="L1243">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1244">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1245">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1246">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1247">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1248">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1249">HREF_FOR_MLD = 0.0              !   [m] default = 0.0</span>
<span id="L1250">                                ! Reference depth used to calculate the potential density used to find the mixed</span>
<span id="L1251">                                ! layer depth based on a delta rho = 0.03 kg/m3.</span>
<span id="L1252">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1253">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1254">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1255">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1256">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1257">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1258">                                ! base of the mixed layer.</span>
<span id="L1259"></span>
<span id="L1260">! === module MOM_CVMix_KPP ===</span>
<span id="L1261">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1262">! See http://cvmix.github.io/</span>
<span id="L1263">USE_KPP = True                  !   [Boolean] default = False</span>
<span id="L1264">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1265">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1266">KPP%</span>
<span id="L1267">PASSIVE = True                  !   [Boolean] default = False</span>
<span id="L1268">                                ! If True, puts KPP into a passive-diagnostic mode.</span>
<span id="L1269">APPLY_NONLOCAL_TRANSPORT = False !   [Boolean] default = False</span>
<span id="L1270">                                ! If True, applies the non-local transport to all tracers. If False, calculates</span>
<span id="L1271">                                ! the non-local transport and tendencies but purely for diagnostic purposes.</span>
<span id="L1272">N_SMOOTH = 0                    ! default = 0</span>
<span id="L1273">                                ! The number of times the 1-1-4-1-1 Laplacian filter is applied on OBL depth.</span>
<span id="L1274">RI_CRIT = 0.3                   !   [nondim] default = 0.3</span>
<span id="L1275">                                ! Critical bulk Richardson number used to define depth of the surface Ocean</span>
<span id="L1276">                                ! Boundary Layer (OBL).</span>
<span id="L1277">VON_KARMAN = 0.4                !   [nondim] default = 0.4</span>
<span id="L1278">                                ! von Karman constant.</span>
<span id="L1279">ENHANCE_DIFFUSION = True        !   [Boolean] default = True</span>
<span id="L1280">                                ! If True, adds enhanced diffusion at the based of the boundary layer.</span>
<span id="L1281">INTERP_TYPE = &quot;quadratic&quot;       ! default = &quot;quadratic&quot;</span>
<span id="L1282">                                ! Type of interpolation to determine the OBL depth.</span>
<span id="L1283">                                ! Allowed types are: linear, quadratic, cubic.</span>
<span id="L1284">INTERP_TYPE2 = &quot;LMD94&quot;          ! default = &quot;LMD94&quot;</span>
<span id="L1285">                                ! Type of interpolation to compute diff and visc at OBL_depth.</span>
<span id="L1286">                                ! Allowed types are: linear, quadratic, cubic or LMD94.</span>
<span id="L1287">STOKES_MOST = False             !   [Boolean] default = False</span>
<span id="L1288">                                ! If True, use Stokes Similarity package.</span>
<span id="L1289">COMPUTE_EKMAN = False           !   [Boolean] default = False</span>
<span id="L1290">                                ! If True, limit OBL depth to be no deeper than Ekman depth.</span>
<span id="L1291">COMPUTE_MONIN_OBUKHOV = False   !   [Boolean] default = False</span>
<span id="L1292">                                ! If True, limit the OBL depth to be no deeper than Monin-Obukhov depth.</span>
<span id="L1293">CS = 98.96                      !   [nondim] default = 98.96</span>
<span id="L1294">                                ! Parameter for computing velocity scale function.</span>
<span id="L1295">CS2 = 6.32739901508             !   [nondim] default = 6.32739901508</span>
<span id="L1296">                                ! Parameter for computing non-local term.</span>
<span id="L1297">DEEP_OBL_OFFSET = 0.0           !   [m] default = 0.0</span>
<span id="L1298">                                ! If non-zero, the distance above the bottom to which the OBL is clipped if it</span>
<span id="L1299">                                ! would otherwise reach the bottom. The smaller of this and 0.1D is used.</span>
<span id="L1300">FIXED_OBLDEPTH = False          !   [Boolean] default = False</span>
<span id="L1301">                                ! If True, fix the OBL depth to FIXED_OBLDEPTH_VALUE rather than using the OBL</span>
<span id="L1302">                                ! depth from CVMix. This option is just for testing purposes.</span>
<span id="L1303">FIXED_OBLDEPTH_VALUE = 30.0     !   [m] default = 30.0</span>
<span id="L1304">                                ! Value for the fixed OBL depth when fixedOBLdepth==True. This parameter is for</span>
<span id="L1305">                                ! just for testing purposes. It will over-ride the OBLdepth computed from CVMix.</span>
<span id="L1306">SURF_LAYER_EXTENT = 0.1         !   [nondim] default = 0.1</span>
<span id="L1307">                                ! Fraction of OBL depth considered in the surface layer.</span>
<span id="L1308">MINIMUM_OBL_DEPTH = 0.0         !   [m] default = 0.0</span>
<span id="L1309">                                ! If non-zero, a minimum depth to use for KPP OBL depth. Independent of this</span>
<span id="L1310">                                ! parameter, the OBL depth is always at least as deep as the first layer.</span>
<span id="L1311">MINIMUM_VT2 = 1.0E-10           !   [m2/s2] default = 1.0E-10</span>
<span id="L1312">                                ! Min of the unresolved velocity Vt2 used in Rib CVMix calculation.</span>
<span id="L1313">                                ! Scaling: MINIMUM_VT2 = const1*d*N*ws, with d=1m, N=1e-5/s, ws=1e-6 m/s.</span>
<span id="L1314">NLT_SHAPE = &quot;CVMix&quot;             ! default = &quot;CVMix&quot;</span>
<span id="L1315">                                ! MOM6 method to set nonlocal transport profile. Over-rides the result from</span>
<span id="L1316">                                ! CVMix.  Allowed values are:</span>
<span id="L1317">                                !    CVMix     - Uses the profiles from CVMix specified by MATCH_TECHNIQUE</span>
<span id="L1318">                                !    LINEAR    - A linear profile, 1-sigma</span>
<span id="L1319">                                !    PARABOLIC - A parablic profile, (1-sigma)^2</span>
<span id="L1320">                                !    CUBIC     - A cubic profile, (1-sigma)^2(1+2*sigma)</span>
<span id="L1321">                                !    CUBIC_LMD - The original KPP profile</span>
<span id="L1322">MATCH_TECHNIQUE = &quot;SimpleShapes&quot; ! default = &quot;SimpleShapes&quot;</span>
<span id="L1323">                                ! CVMix method to set profile function for diffusivity and NLT, as well as</span>
<span id="L1324">                                ! matching across OBL base. Allowed values are:</span>
<span id="L1325">                                !    SimpleShapes      = sigma*(1-sigma)^2 for both diffusivity and NLT</span>
<span id="L1326">                                !    MatchGradient     = sigma*(1-sigma)^2 for NLT; diffusivity profile from</span>
<span id="L1327">                                !      matching</span>
<span id="L1328">                                !    MatchBoth         = match gradient for both diffusivity and NLT</span>
<span id="L1329">                                !    ParabolicNonLocal = sigma*(1-sigma)^2 for diffusivity; (1-sigma)^2 for NLT</span>
<span id="L1330">KPP_ZERO_DIFFUSIVITY = False    !   [Boolean] default = False</span>
<span id="L1331">                                ! If True, zeroes the KPP diffusivity and viscosity; for testing purpose.</span>
<span id="L1332">KPP_IS_ADDITIVE = True          !   [Boolean] default = True</span>
<span id="L1333">                                ! If true, adds KPP diffusivity to diffusivity from other schemes.</span>
<span id="L1334">                                ! If false, KPP is the only diffusivity wherever KPP is non-zero.</span>
<span id="L1335">KPP_SHORTWAVE_METHOD = &quot;MXL_SW&quot; ! default = &quot;MXL_SW&quot;</span>
<span id="L1336">                                ! Determines contribution of shortwave radiation to KPP surface buoyancy flux.</span>
<span id="L1337">                                ! Options include:</span>
<span id="L1338">                                !   ALL_SW: use total shortwave radiation</span>
<span id="L1339">                                !   MXL_SW: use shortwave radiation absorbed by mixing layer</span>
<span id="L1340">                                !   LV1_SW: use shortwave radiation absorbed by top model layer</span>
<span id="L1341">CVMix_ZERO_H_WORK_AROUND = 0.0  !   [m] default = 0.0</span>
<span id="L1342">                                ! A minimum thickness used to avoid division by small numbers in the vicinity of</span>
<span id="L1343">                                ! vanished layers. This is independent of MIN_THICKNESS used in other parts of</span>
<span id="L1344">                                ! MOM.</span>
<span id="L1345">USE_KPP_LT_K = False            !   [Boolean] default = False</span>
<span id="L1346">                                ! Flag for Langmuir turbulence enhancement of turbulentmixing coefficient.</span>
<span id="L1347">STOKES_MIXING = False           !   [Boolean] default = False</span>
<span id="L1348">                                ! Flag for Langmuir turbulence enhancement of turbulentmixing coefficient.</span>
<span id="L1349">USE_KPP_LT_VT2 = False          !   [Boolean] default = False</span>
<span id="L1350">                                ! Flag for Langmuir turbulence enhancement of Vt2in Bulk Richardson Number.</span>
<span id="L1351">KPP_CVt2 = 1.6                  !   [nondim] default = 1.6</span>
<span id="L1352">                                ! Parameter for Stokes MOST convection entrainment</span>
<span id="L1353">ANSWER_DATE = 99991231          ! default = 99991231</span>
<span id="L1354">                                ! The vintage of the order of arithmetic in the CVMix KPP calculations.  Values</span>
<span id="L1355">                                ! below 20240501 recover the answers from early in 2024, while higher values use</span>
<span id="L1356">                                ! expressions that have been refactored for rotational symmetry.</span>
<span id="L1357">%KPP</span>
<span id="L1358"></span>
<span id="L1359">! === module MOM_CVMix_conv ===</span>
<span id="L1360">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1361">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1362">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1363">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1364">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1365"></span>
<span id="L1366">! === module MOM_set_diffusivity ===</span>
<span id="L1367">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1368">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1369">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1370">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1371">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1372">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1373">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1374">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1375">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1376">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1377"></span>
<span id="L1378">! === module MOM_tidal_mixing ===</span>
<span id="L1379">! Vertical Tidal Mixing Parameterization</span>
<span id="L1380">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1381">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1382">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1383">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1384">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1385">ML_RADIATION = True             !   [Boolean] default = False</span>
<span id="L1386">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1387">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1388">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1389">ML_RAD_EFOLD_COEFF = 0.2        !   [nondim] default = 0.2</span>
<span id="L1390">                                ! A coefficient that is used to scale the penetration depth for turbulence below</span>
<span id="L1391">                                ! the base of the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1392">ML_RAD_BUG = False              !   [Boolean] default = False</span>
<span id="L1393">                                ! If true use code with a bug that reduces the energy available in the</span>
<span id="L1394">                                ! transition layer by a factor of the inverse of the energy deposition</span>
<span id="L1395">                                ! lenthscale (in m).</span>
<span id="L1396">ML_RAD_KD_MAX = 0.001           !   [m2 s-1] default = 0.001</span>
<span id="L1397">                                ! The maximum diapycnal diffusivity due to turbulence radiated from the base of</span>
<span id="L1398">                                ! the mixed layer. This is only used if ML_RADIATION is true.</span>
<span id="L1399">ML_RAD_COEFF = 0.2              !   [nondim] default = 0.2</span>
<span id="L1400">                                ! The coefficient which scales MSTAR*USTAR^3 to obtain the energy available for</span>
<span id="L1401">                                ! mixing below the base of the mixed layer. This is only used if ML_RADIATION is</span>
<span id="L1402">                                ! true.</span>
<span id="L1403">ML_RAD_APPLY_TKE_DECAY = True   !   [Boolean] default = True</span>
<span id="L1404">                                ! If true, apply the same exponential decay to ML_rad as is applied to the other</span>
<span id="L1405">                                ! surface sources of TKE in the mixed layer code. This is only used if</span>
<span id="L1406">                                ! ML_RADIATION is true.</span>
<span id="L1407">MSTAR = 1.2                     !   [nondim] default = 1.2</span>
<span id="L1408">                                ! The ratio of the friction velocity cubed to the TKE input to the mixed layer.</span>
<span id="L1409">TKE_DECAY = 10.0                !   [nondim] default = 2.5</span>
<span id="L1410">                                ! The ratio of the natural Ekman depth to the TKE decay scale.</span>
<span id="L1411">ML_OMEGA_FRAC = 1.0             !   [nondim] default = 0.0</span>
<span id="L1412">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L1413">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L1414">                                ! of*4*omega^2).</span>
<span id="L1415">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L1416">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1417">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1418">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1419">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1420">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1421">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1422">BBL_MIXING_AS_MAX = True        !   [Boolean] default = True</span>
<span id="L1423">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1424">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1425">USE_LOTW_BBL_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1426">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1427">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1428">                                ! scheme.</span>
<span id="L1429">DRAG_DIFFUSIVITY_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1430">                                ! The vintage of the order of arithmetic in the drag diffusivity calculations.</span>
<span id="L1431">                                ! Values above 20250301 use less confusing expressions to set the bottom-drag</span>
<span id="L1432">                                ! generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1433">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1434">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1435">                                ! boundary layer density.</span>
<span id="L1436">SIMPLE_TKE_TO_KD = False        !   [Boolean] default = False</span>
<span id="L1437">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L1438">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L1439">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L1440"></span>
<span id="L1441">! === module MOM_bkgnd_mixing ===</span>
<span id="L1442">! Adding static vertical background mixing coefficients</span>
<span id="L1443">KD = 2.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1444">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1445">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1446">KD_MIN = 2.0E-06                !   [m2 s-1] default = 2.0E-07</span>
<span id="L1447">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1448">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1449">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1450">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1451">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1452">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1453">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1454">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1455">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1456">                                ! into viscosities.</span>
<span id="L1457">HENYEY_IGW_BACKGROUND = False   !   [Boolean] default = False</span>
<span id="L1458">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1459">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1460">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1461">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1462">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1463">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1464">KD_MAX = -1.0                   !   [m2 s-1] default = -1.0</span>
<span id="L1465">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1466">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1467">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1468">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1469">                                ! or scaling.</span>
<span id="L1470">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1471">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1472">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1473">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1474">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1475">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1476">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1477">                                ! = A + B*N.</span>
<span id="L1478">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1479">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1480">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1481">                                ! = A + B*N</span>
<span id="L1482">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1483">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1484">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L1485">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1486">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1487"></span>
<span id="L1488">! === module MOM_kappa_shear ===</span>
<span id="L1489">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1490">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1491">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1492">                                ! parameterization.</span>
<span id="L1493">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L1494">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1495">                                ! (i.e., the vorticity points).</span>
<span id="L1496">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L1497">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L1498">                                ! tracer points in the kappa shear solver.</span>
<span id="L1499">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L1500">                                ! The critical Richardson number for shear mixing.</span>
<span id="L1501">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L1502">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L1503">                                ! values in the range of 0.085-0.089.</span>
<span id="L1504">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L1505">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L1506">                                ! number driven mixing.</span>
<span id="L1507">KD_KAPPA_SHEAR_0 = 2.0E-05      !   [m2 s-1] default = 2.0E-05</span>
<span id="L1508">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L1509">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L1510">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L1511">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L1512">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L1513">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L1514">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L1515">KD_TRUNC_KAPPA_SHEAR = 2.0E-07  !   [m2 s-1] default = 2.0E-07</span>
<span id="L1516">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L1517">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L1518">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L1519">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L1520">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L1521">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L1522">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L1523">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L1524">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L1525">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L1526">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L1527">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L1528">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L1529">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L1530">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1531">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L1532">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L1533">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1534">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L1535">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L1536">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L1537">                                ! the growth of shear instabilies [nondim].</span>
<span id="L1538">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L1539">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L1540">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L1541">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L1542">                                ! errors than this.</span>
<span id="L1543">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L1544">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L1545">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L1546">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L1547">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L1548">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L1549">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L1550">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L1551">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L1552">                                ! time-averaged diffusivity.</span>
<span id="L1553">PRANDTL_TURB = 1.0              !   [nondim] default = 1.0</span>
<span id="L1554">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L1555">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L1556">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L1557">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L1558">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L1559">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L1560">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L1561">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L1562">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L1563">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L1564">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L1565">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L1566">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L1567">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L1568">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L1569">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L1570">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L1571">                                ! less restrictive check.</span>
<span id="L1572"></span>
<span id="L1573">! === module MOM_CVMix_shear ===</span>
<span id="L1574">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L1575">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L1576">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L1577">                                ! parameterization.</span>
<span id="L1578">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L1579">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L1580">                                ! parameterization.</span>
<span id="L1581"></span>
<span id="L1582">! === module MOM_CVMix_ddiff ===</span>
<span id="L1583">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L1584">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L1585">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L1586">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L1587">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L1588"></span>
<span id="L1589">! === module MOM_diabatic_aux ===</span>
<span id="L1590">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L1591">RECLAIM_FRAZIL = False          !   [Boolean] default = True</span>
<span id="L1592">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L1593">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L1594">                                ! is above the freezing point.</span>
<span id="L1595">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L1596">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L1597">                                ! net surface salt fluxes within a timestep.</span>
<span id="L1598">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L1599">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L1600">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L1601">                                ! cavities.</span>
<span id="L1602">IGNORE_FLUXES_OVER_LAND = False !   [Boolean] default = False</span>
<span id="L1603">                                ! If true, the model does not check if fluxes are being applied over land</span>
<span id="L1604">                                ! points. This is needed when the ocean is coupled with ice shelves and sea ice,</span>
<span id="L1605">                                ! since the sea ice mask needs to be different than the ocean mask to avoid sea</span>
<span id="L1606">                                ! ice formation under ice shelves. This flag only works when use_ePBL = True.</span>
<span id="L1607">DO_RIVERMIX = False             !   [Boolean] default = False</span>
<span id="L1608">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L1609">                                ! down to RIVERMIX_DEPTH if the ocean is that deep.</span>
<span id="L1610">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L1611">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L1612">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L1613">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L1614">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L1615">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L1616">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L1617">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L1618">VAR_PEN_SW = True               !   [Boolean] default = False</span>
<span id="L1619">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L1620">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L1621">CHL_FROM_FILE = True            !   [Boolean] default = True</span>
<span id="L1622">                                ! If true, chl_a is read from a file.</span>
<span id="L1623">CHL_FILE = &quot;forcing_monthly.nc&quot; !</span>
<span id="L1624">                                ! CHL_FILE is the file containing chl_a concentrations in the variable CHL_A. It</span>
<span id="L1625">                                ! is used when VAR_PEN_SW and CHL_FROM_FILE are true.</span>
<span id="L1626">CHL_VARNAME = &quot;CHL_A&quot;           ! default = &quot;CHL_A&quot;</span>
<span id="L1627">                                ! Name of CHL_A variable in CHL_FILE.</span>
<span id="L1628"></span>
<span id="L1629">! === module MOM_energetic_PBL ===</span>
<span id="L1630">EKMAN_SCALE_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L1631">                                ! A nondimensional scaling factor controlling the inhibition of the diffusive</span>
<span id="L1632">                                ! length scale by rotation. Making this larger decreases the PBL diffusivity.</span>
<span id="L1633">EPBL_ANSWER_DATE = 20231231     ! default = 99991231</span>
<span id="L1634">                                ! The vintage of the order of arithmetic and expressions in the energetic PBL</span>
<span id="L1635">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1636">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1637">                                ! Values below 20240101 use A**(1./3.) to estimate the cube root of A in several</span>
<span id="L1638">                                ! expressions, while higher values use the integer root function cuberoot(A) and</span>
<span id="L1639">                                ! therefore can work with scaled variables.</span>
<span id="L1640">EPBL_ORIGINAL_PE_CALC = True    !   [Boolean] default = True</span>
<span id="L1641">                                ! If true, the ePBL code uses the original form of the potential energy change</span>
<span id="L1642">                                ! code.  Otherwise, the newer version that can work with successive increments</span>
<span id="L1643">                                ! to the diffusivity in upward or downward passes is used.</span>
<span id="L1644">MKE_TO_TKE_EFFIC = 0.0          !   [nondim] default = 0.0</span>
<span id="L1645">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L1646">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L1647">DIRECT_EPBL_MIXING_CALC = False !   [Boolean] default = False</span>
<span id="L1648">                                ! If true and there is no conversion from mean kinetic energy to ePBL turbulent</span>
<span id="L1649">                                ! kinetic energy, use a direct calculation of the diffusivity that is supported</span>
<span id="L1650">                                ! by a given energy input instead of the more general but slower iterative</span>
<span id="L1651">                                ! solver.</span>
<span id="L1652">EPBL_MSTAR_SCHEME = &quot;CONSTANT&quot;  ! default = &quot;CONSTANT&quot;</span>
<span id="L1653">                                ! EPBL_MSTAR_SCHEME selects the method for setting mstar.  Valid values are:</span>
<span id="L1654">                                !    CONSTANT   - Use a fixed mstar given by MSTAR</span>
<span id="L1655">                                !    OM4        - Use L_Ekman/L_Obukhov in the stabilizing limit, as in OM4</span>
<span id="L1656">                                !    REICHL_H18 - Use the scheme documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L1657">EPBL_BBL_USE_MSTAR = False      !   [nondim] default = False</span>
<span id="L1658">                                ! A logical to use mstar in the calculation of TKE in the ePBL BBL scheme</span>
<span id="L1659">NSTAR = 0.2                     !   [nondim] default = 0.2</span>
<span id="L1660">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L1661">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L1662">                                ! positive.</span>
<span id="L1663">MSTAR_CONV_ADJ = 0.0            !   [nondim] default = 0.0</span>
<span id="L1664">                                ! Coefficient used for reducing mstar during convection due to reduction of</span>
<span id="L1665">                                ! stable density gradient.</span>
<span id="L1666">USE_MLD_ITERATION = False       !   [Boolean] default = True</span>
<span id="L1667">                                ! A logical that specifies whether or not to use the distance to the bottom of</span>
<span id="L1668">                                ! the actively turbulent boundary layer to help set the EPBL length scale.</span>
<span id="L1669">EPBL_TRANSITION_SCALE = 0.1     !   [nondim] default = 0.1</span>
<span id="L1670">                                ! A scale for the mixing length in the transition layer at the edge of the</span>
<span id="L1671">                                ! boundary layer as a fraction of the boundary layer thickness.</span>
<span id="L1672">EPBL_MIN_MIX_LEN = 0.0          !   [meter] default = 0.0</span>
<span id="L1673">                                ! The minimum mixing length scale that will be used by ePBL.  The default (0)</span>
<span id="L1674">                                ! does not set a minimum.</span>
<span id="L1675">MIX_LEN_EXPONENT = 2.0          !   [nondim] default = 2.0</span>
<span id="L1676">                                ! The exponent applied to the ratio of the distance to the MLD and the MLD depth</span>
<span id="L1677">                                ! which determines the shape of the mixing length. This is only used if</span>
<span id="L1678">                                ! USE_MLD_ITERATION is True.</span>
<span id="L1679">EPBL_VEL_SCALE_SCHEME = &quot;CUBE_ROOT_TKE&quot; ! default = &quot;CUBE_ROOT_TKE&quot;</span>
<span id="L1680">                                ! Selects the method for translating TKE into turbulent velocities. Valid values</span>
<span id="L1681">                                ! are:</span>
<span id="L1682">                                !    CUBE_ROOT_TKE  - A constant times the cube root of remaining TKE.</span>
<span id="L1683">                                !    REICHL_H18 - Use the scheme based on a combination of w* and v* as</span>
<span id="L1684">                                !                 documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L1685">WSTAR_USTAR_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L1686">                                ! A ratio relating the efficiency with which convectively released energy is</span>
<span id="L1687">                                ! converted to a turbulent velocity, relative to mechanically forced TKE. Making</span>
<span id="L1688">                                ! this larger increases the BL diffusivity</span>
<span id="L1689">EPBL_VEL_SCALE_FACTOR = 1.0     !   [nondim] default = 1.0</span>
<span id="L1690">                                ! An overall nondimensional scaling factor for wT. Making this larger increases</span>
<span id="L1691">                                ! the PBL diffusivity.</span>
<span id="L1692">VSTAR_SURF_FAC = 1.2            !   [nondim] default = 1.2</span>
<span id="L1693">                                ! The proportionality times ustar to set vstar at the surface.</span>
<span id="L1694">EPBL_BBL_EFFIC = 0.0            !   [nondim] default = 0.0</span>
<span id="L1695">                                ! The efficiency of bottom boundary layer mixing via ePBL.  Setting this to a</span>
<span id="L1696">                                ! value that is greater than 0 to enable bottom boundary layer mixing from EPBL.</span>
<span id="L1697">EPBL_BBL_TIDAL_EFFIC = 0.0      !   [nondim] default = 0.0</span>
<span id="L1698">                                ! The efficiency of bottom boundary layer mixing via ePBL driven by the bottom</span>
<span id="L1699">                                ! drag dissipation of tides, as provided in fluxes%BBL_tidal_dis.</span>
<span id="L1700">USE_LA_LI2016 = False           !   [Boolean] default = False</span>
<span id="L1701">                                ! A logical to use the Li et al. 2016 (submitted) formula to determine the</span>
<span id="L1702">                                ! Langmuir number.</span>
<span id="L1703">EPBL_LT = False                 !   [Boolean] default = False</span>
<span id="L1704">                                ! A logical to use a LT parameterization.</span>
<span id="L1705">EPBL_EQD_DIFFUSIVITY_SHAPE = False !   [nondim] default = False</span>
<span id="L1706">                                ! Logical flag for activating ML equation for shape function that uses forcing</span>
<span id="L1707">                                ! to change its structure.</span>
<span id="L1708">EPBL_EQD_DIFFUSIVITY_VELOCITY = False !   [nondim] default = False</span>
<span id="L1709">                                ! Logical flag for activating ML equation discovery for velocity scale</span>
<span id="L1710">EPBL_EQD_DIFFUSIVITY_VELOCITY_H = False !   [nondim] default = False</span>
<span id="L1711">                                ! Logical flag for activating ML equation discovery for velocity scale with h as</span>
<span id="L1712">                                ! input</span>
<span id="L1713">EPBL_OPTIONS_DIFF = 0           ! default = 0</span>
<span id="L1714">                                ! If positive, this is a coded integer indicating a pair of settings whose</span>
<span id="L1715">                                ! differences are diagnosed in a passive diagnostic mode  via extra calls to</span>
<span id="L1716">                                ! ePBL_column.  If this is 0 or negative no extra calls occur.</span>
<span id="L1717">!EPBL_USTAR_MIN = 1.45842E-18   !   [m s-1]</span>
<span id="L1718">                                ! The (tiny) minimum friction velocity used within the ePBL code, derived from</span>
<span id="L1719">                                ! OMEGA and ANGSTROM.</span>
<span id="L1720"></span>
<span id="L1721">! === module MOM_regularize_layers ===</span>
<span id="L1722">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L1723">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L1724">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L1725"></span>
<span id="L1726">! === module MOM_opacity ===</span>
<span id="L1727">OPACITY_SCHEME = &quot;MANIZZA_05&quot;   ! default = &quot;MANIZZA_05&quot;</span>
<span id="L1728">                                ! This character string specifies how chlorophyll concentrations are translated</span>
<span id="L1729">                                ! into opacities. Currently valid options include:</span>
<span id="L1730">                                !        MANIZZA_05 - Use Manizza et al., GRL, 2005.</span>
<span id="L1731">                                !        MOREL_88 - Use Morel, JGR, 1988.</span>
<span id="L1732">                                !        OHLMANN_03 - Use Ohlmann, J Clim, 2003. (only use if dz(1)&gt;2.0m)</span>
<span id="L1733">BLUE_FRAC_SW = 0.5              !   [nondim] default = 0.5</span>
<span id="L1734">                                ! The fraction of the penetrating shortwave radiation that is in the blue band.</span>
<span id="L1735">PEN_SW_NBANDS = 3               ! default = 1</span>
<span id="L1736">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L1737">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L1738">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L1739">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1740">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1741">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L1742">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L1743">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L1744">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L1745">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L1746">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L1747">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L1748">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L1749">OPACITY_VALUES_MANIZZA = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 !   [m-1] default = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0</span>
<span id="L1750">                                ! Pairs of opacity coefficients for blue, red and near-infrared radiation with</span>
<span id="L1751">                                ! parameterizations following the functional form from Manizza et al., GRL 2005,</span>
<span id="L1752">                                ! namely in the form opacity = coef_1 + coef_2 * chl**pow for each band.</span>
<span id="L1753">                                ! Although coefficients are set for 3 bands, more or less bands may actually be</span>
<span id="L1754">                                ! used, with extra bands following the same properties as band 3.</span>
<span id="L1755">CHOROPHYLL_POWER_MANIZZA = 0.674, 0.629, 0.0 !   [nondim] default = 0.674, 0.629, 0.0</span>
<span id="L1756">                                ! Powers of chlorophyll for blue, red and near-infrared radiation bands in</span>
<span id="L1757">                                ! expressions for opacity of the form opacity = coef_1 + coef_2 * chl**pow.</span>
<span id="L1758">OPACITY_BAND_WAVELENGTHS = 0.0, 550.0, 700.0, 2800.0 !   [nm] default = 0.0, 550.0, 700.0, 2800.0</span>
<span id="L1759">                                ! The bounding wavelengths for the various bands of shortwave radiation, with</span>
<span id="L1760">                                ! defaults that depend on the setting for OPACITY_SCHEME.</span>
<span id="L1761">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L1762">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L1763">                                ! muddy water.</span>
<span id="L1764"></span>
<span id="L1765">! === module MOM_tracer_advect ===</span>
<span id="L1766">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L1767">                                ! The horizontal transport scheme for tracers:</span>
<span id="L1768">                                !   PLM    - Piecewise Linear Method</span>
<span id="L1769">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L1770">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L1771"></span>
<span id="L1772">! === module MOM_tracer_hor_diff ===</span>
<span id="L1773">KHTR = 600.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1774">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L1775">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1776">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L1777">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1778">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L1779">                                ! activate.</span>
<span id="L1780">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L1781">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L1782">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L1783">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L1784">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L1785">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L1786">                                ! tracers to thickness mixing.</span>
<span id="L1787">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L1788">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L1789">                                ! interior.</span>
<span id="L1790">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L1791">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L1792">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L1793">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L1794">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L1795">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L1796">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L1797">                                ! iterations is often this value or the next greater integer.</span>
<span id="L1798">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L1799">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L1800">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L1801">                                ! positions of the surfaces do not change</span>
<span id="L1802"></span>
<span id="L1803">! === module MOM_neutral_diffusion ===</span>
<span id="L1804">! This module implements neutral diffusion of tracers</span>
<span id="L1805">USE_NEUTRAL_DIFFUSION = False   !   [Boolean] default = False</span>
<span id="L1806">                                ! If true, enables the neutral diffusion module.</span>
<span id="L1807"></span>
<span id="L1808">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L1809">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L1810">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L1811">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L1812">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L1813">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L1814">                                ! error rather than issue a WARNING.</span>
<span id="L1815"></span>
<span id="L1816">! === module MOM_sum_output ===</span>
<span id="L1817">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L1818">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L1819">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L1820">                                ! dramatically.</span>
<span id="L1821">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L1822">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L1823">                                ! are written.</span>
<span id="L1824">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L1825">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L1826">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L1827">                                ! to stop if there is any truncation of velocities.</span>
<span id="L1828">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L1829">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L1830">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L1831">                                ! 10*MAXVEL^2.</span>
<span id="L1832">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L1833">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L1834">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L1835">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L1836">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L1837">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L1838">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L1839">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L1840">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L1841">                                ! The time unit in seconds a number of input fields</span>
<span id="L1842">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L1843">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L1844">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L1845">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L1846">                                ! file.</span>
<span id="L1847">ENERGYSAVEDAYS = 10.0           !   [days] default = 1.0</span>
<span id="L1848">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L1849">                                ! other globally summed diagnostics.</span>
<span id="L1850">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L1851">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L1852">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L1853">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L1854"></span>
<span id="L1855">! === module ocean_stochastics_init ===</span>
<span id="L1856">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L1857">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L1858">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L1859">                                ! UFS model only.</span>
<span id="L1860">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L1861">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L1862">                                ! energy backscatter scheme.</span>
<span id="L1863">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L1864">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L1865">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L1866">                                ! namelist in the UFS model only.</span>
<span id="L1867"></span>
<span id="L1868">! === module MOM_surface_forcing ===</span>
<span id="L1869">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L1870">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L1871">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L1872">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L1873">                                ! model.</span>
<span id="L1874">BUOY_CONFIG = &quot;data_override&quot;   ! default = &quot;zero&quot;</span>
<span id="L1875">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L1876">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L1877">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L1878">WIND_CONFIG = &quot;data_override&quot;   ! default = &quot;zero&quot;</span>
<span id="L1879">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L1880">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L1881">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L1882">RESTOREBUOY = False             !   [Boolean] default = False</span>
<span id="L1883">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L1884">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L1885">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L1886">                                ! The latent heat of fusion.</span>
<span id="L1887">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L1888">                                ! The latent heat of fusion.</span>
<span id="L1889">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L1890">                                ! The background gustiness in the winds.</span>
<span id="L1891">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L1892">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L1893">                                ! velocity</span>
<span id="L1894">READ_GUST_2D = True             !   [Boolean] default = False</span>
<span id="L1895">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L1896">GUST_2D_FILE = &quot;forcing_monthly.nc&quot; !</span>
<span id="L1897">                                ! The file in which the wind gustiness is found in variable gustiness.</span>
<span id="L1898"></span>
<span id="L1899">! === module MOM_restart ===</span>
<span id="L1900">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L1901">                                ! If true, enables surface wave modules.</span>
<span id="L1902"></span>
<span id="L1903">! === module MOM_main (MOM_driver) ===</span>
<span id="L1904">DT_FORCING = 3600.0             !   [s] default = 3600.0</span>
<span id="L1905">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L1906">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L1907">DAYMAX = 180.0                  !   [days]</span>
<span id="L1908">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L1909">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L1910">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L1911">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L1912">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L1913">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L1914">RESTART_CONTROL = 0             ! default = 1</span>
<span id="L1915">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L1916">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L1917">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L1918">                                ! non-negative value.</span>
<span id="L1919">RESTINT = 3650.0                !   [days] default = 0.0</span>
<span id="L1920">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L1921">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L1922">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L1923">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L1924">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L1925">                                ! an elapsed CPU time.</span>
<span id="L1926"></span>
<span id="L1927">! === module MOM_write_cputime ===</span>
<span id="L1928">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L1929">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L1930">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L1931">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L1932">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L1933">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L1934">                                ! processors used.</span>
<span id="L1935">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L1936">                                ! The file into which CPU time is written.</span>
<span id="L1937"></span>
<span id="L1938">! === module MOM_file_parser ===</span>
<span id="L1939">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L1940">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L1941">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L1942">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L1943">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L1944">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L1945">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L1946">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L1947">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L1948">                                ! MOM_parameter_doc.short .</span>
</pre>
